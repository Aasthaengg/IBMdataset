class Dice:
    def __init__(self):
        self.up = 1
        self.under = 6
        self.N = 5
        self.W = 4
        self.E = 3
        self.S = 2

    def roll(self, d):#d => direction
        if d == "N":
            tmp = self.up
            self.up = self.S
            self.S = self.under
            self.under = self.N
            self.N = tmp
        elif d == "W":
            tmp = self.up
            self.up = self.E
            self.E = self.under
            self.under = self.W
            self.W = tmp
        elif d == "E":
            tmp = self.up
            self.up = self.W
            self.W = self.under
            self.under = self.E
            self.E = tmp
        elif d == "S":
            tmp = self.up
            self.up = self.N
            self.N = self.under
            self.under = self.S
            self.S = tmp

    def getUpward(self):
        return self.up

    def setRoll(self,up,under,N,W,E,S):
        self.up = up
        self.under = under
        self.N = N
        self.W = W
        self.E = E
        self.S = S

myd = Dice()
myd.up, myd.S, myd.E, myd.W, myd.N, myd.under = map(int,input().split())
do = input()
for i in do:
        myd.roll(i)
print(myd.getUpward())