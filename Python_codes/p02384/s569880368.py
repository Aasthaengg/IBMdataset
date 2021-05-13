import math

class Dice():
    top   = 0 #上
    left  = 0 #左
    right = 0 #右
    front = 0 #前面
    back  = 0 #後面
    below = 0 #真下

    DEBUG_MODE = False
    def __init__(self,lst,dbg = False):
        if len(lst) == 6:
            self.top   = lst[0]
            self.front = lst[1]
            self.right = lst[2]
            self.left  = lst[3]
            self.back  = lst[4]
            self.below = lst[5]

        if dbg == True:
            self.DEBUG_MODE = True
        else:
            self.DEBUG_MODE = False
    
    def rotate(self,string):
        
        for ch in string:
            if   ch == 'W':
                self.left,self.top,self.right,self.below = self.top,self.right,self.below,self.left

            elif ch == 'E':
                self.left,self.top,self.right,self.below = self.below,self.left,self.top,self.right

            elif ch == 'S':
                self.top,self.back,self.below,self.front = self.back,self.below,self.front,self.top

            elif ch == 'N':
                self.top,self.back,self.below,self.front = self.front,self.top,self.back,self.below
            
            # デバッグモードなら全部の値をモニタする
            if self.DEBUG_MODE:
                self.dbg_PRINT_ALL_VALUE()

    def front_and_top_to_right(self,top,front):

        for i in range(4):
            for j in range(4):
                if self.top == top and self.front == front:
                    return self.right
                self.rotate("W")
            self.rotate("S")
        
        self.rotate("NES") #ヨコ回転
        
        for i in range(2):
            for j in range(4):
                if self.top == top and self.front == front:
                    return self.right
                self.rotate("W")
            self.rotate("SS")
        
        return None


        
    def get_topvalue(self):
        return self.top
    
    def dbg_PRINT_ALL_VALUE(self):
        print(f"        bk:{self.back:04} ")
        print(f"le:{self.left:04} tp:{self.top:04} ri:{self.right:04} be:{self.below:04}")
        print(f"        fr:{self.front:04} ")

lst = list(map(int,input().split()))
#lst = [1,2,3,4,5,6]
rep = int(input())
for i in range(rep):
    dice = Dice(lst)
    top,front = list(map(int,input().split()))
    print(dice.front_and_top_to_right(top,front))
