class Dice:
    def __init__(self, top, dside):
        self.top = top
        self.dside = dside
        self.rside = None
        self.num = [self.top, self.dside, 7-self.top, 7-self.dside]
    def rside_num(self):
        if 2 in self.num and 3 in self.num:
            if(self.num.index(3)==self.num.index(2)+1 or 
                self.num==[3, 5, 4, 2]):
                self.rside = 1
            else:
                self.rside = 6
        elif 1 in self.num and 4 in self.num:
            if(self.num.index(4)==self.num.index(1)+1 or 
                self.num==[4, 6, 3, 1]):
                self.rside = 2
            else:
                self.rside = 5
        else:
            if(self.num.index(2)==self.num.index(1)+1 or
                self.num==[2, 6, 5, 1]):
                self.rside = 3
            else:
                self.rside = 4

num = list(map(int, input().split()))
n = int(input())
for i in range(n):
    value = list(map(int, input().split()))
    dice = Dice(num.index(value[0])+1, num.index(value[1])+1)
    dice.rside_num()
    print(num[dice.rside-1])

