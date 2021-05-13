class Dice:
    
    def __init__(self,ls):
        self.a = ls[1-1] # top
        self.b = ls[2-1] # front
        self.c = ls[3-1] # right
        self.d = ls[4-1] # left
        self.e = ls[5-1] # back
        self.f = ls[6-1] # bottom
    
    def E(self):
        self.a, self.c, self.f, self.d = self.d, self.a, self.c, self.f
    def W(self):
        self.a, self.c, self.f, self.d = self.c, self.f, self.d, self.a
    def S(self):
        self.a, self.b, self.f, self.e = self.e, self.a, self.b, self.f
    def N(self):
        self.a, self.b, self.f, self.e = self.b, self.f, self.e, self.a   
                        
import random
ls = map(int,raw_input().split())
q = int(raw_input())
for i in range(q):
    dice = Dice(ls)
    a,b = map(int,raw_input().split())
    while dice.a != a or dice.b != b:
        i = random.choice([1,2,3,4])
        if i == 1: dice.E()
        elif i == 2: dice.W()
        elif i == 3 : dice.S()
        elif i == 4 : dice.N()
    print dice.c