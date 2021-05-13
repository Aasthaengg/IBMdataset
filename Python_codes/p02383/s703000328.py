class Dice:
    def __init__(self,ls):
        self.a = ls[0]
        self.b = ls[1]
        self.c = ls[2]
        self.d = ls[3]
        self.e = ls[4]
        self.f = ls[5]
    
    def E(self):
        self.a, self.c, self.f, self.d = self.d, self.a, self.c, self.f
    def W(self):
        self.a, self.c, self.f, self.d = self.c, self.f, self.d, self.a
    def S(self):
        self.a, self.b, self.f, self.e = self.e, self.a, self.b, self.f
    def N(self):
        self.a, self.b, self.f, self.e = self.b, self.f, self.e, self.a
    
ls = map(int,raw_input().split())
orders = raw_input()
dice = Dice(ls)
for w in orders:
    if w == 'E': dice.E()
    elif w == 'W': dice.W()
    elif w == 'S': dice.S()
    elif w == 'N': dice.N()
print dice.a