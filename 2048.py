import re
import random
class twenty_fourty_eight():

    def __init__(self):
        """ initialize the game of 2048"""
        # TODO
        self.board = [[0 for x in range(4)] for x in range(4)]
        self.score = 0
        self.input_re = '[wasd]'
        x = random.randint(0,3)
        y = random.randint(0,3)
        self.board[y][x]=4
        # x1 = random.randint(0,3)
        # y1 = random.randint(0,3)
        # while x== x1 and y==y1:
        #     x1 = random.randint(0,3)
        #     y1 = random.randint(0,3)
        # self.board[y1][x1]=2
    def print_board(self):
        """prints the board to the user"""
        board_print = []
        board_print.append('')
        for y_index, y in enumerate(self.board):
            for x in self.board[y_index]:
                if x == 0:
                    board_print.append(' ')
                else:
                    board_print.append(str(x))
            board_print.append('\n')
        board_print = ' | '.join(board_print)
        print(board_print)
        print('score: {0}'.format(self.score))


    def move(self, action):
        """action handeler"""
        if action == 'w':
            for i in range(len(self.board)):
                arr =[]
                for j in range(len(self.board)):
                    arr.append(self.board[j][i])
                print(arr)
                arr= self.__row_move(arr)
                for j in range(len(self.board)):
                    self.board[j][i] = arr[j]


        elif action == 'a':
            for i, x in enumerate(self.board):
                self.board[i]=self.__row_move(x)
        elif action == 's':
            for i in range(len(self.board)):
                arr =[]
                for j in range(len(self.board)):
                    arr.append(self.board[j][i])
                arr= list(reversed(self.__row_move(list(reversed(arr)))))
                for j in range(len(self.board)):
                    self.board[j][i] = arr[j]
            
        elif action == 'd':
            for i, x in enumerate(self.board):
                self.board[i]=list(reversed(self.__row_move(list(reversed(x)))))
            
        
    def __row_move(self, array):
        for i, x in enumerate(array):
            index = i
            for y in range(1, i+1):
                y = i-y
                if x == array[y]:
                    # mergeable
                    array[y]+=x
                    array[i]=0
                    self.score += 2*x
                    break
                elif array[y] ==0:
                   index = y
            
            if index != i:
                temp = array[i]
                array[i]= array[index]
                array[index]= temp
                self.score+=2
        return array
    def random_insert(self):
        zero_count =-1
        for x in self.board:
            zero_count+=x.count(0)
        random_index = random.randint(0,zero_count-1)
        zeros=-1
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j]==0:
                    zeros+=1
                if zeros == random_index:
                    self.board[i][j]=2 if random.random() > 0.05 else 4
                    return 

    def game_over(self):
        """ game over?"""
        for x in self.board:
            for y in x:
                if y == 0:
                    return False
        return True

    def prompt(self):
        """prompts the user"""
        
        userchoice = input("please choose: w, a, s, d >")
        userchoice = userchoice
        if userchoice == 'help':
            print('help instructions')
            return self.prompt()
        elif len(re.search(self.input_re,userchoice ).group()) != 1:
            print('invalid entry')
            return self.prompt()
        
        #found choice
        return userchoice

    def start(self):
        """ game starter"""
        while not self.game_over():
            #prompt
            self.random_insert()
            self.print_board()
            userchoice = self.prompt()
            #move
            self.move(userchoice)
        #raise NotImplementedError()

def main():
    game = twenty_fourty_eight()
    game.start()

if __name__ == '__main__':
    main()