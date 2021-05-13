class Dice:
    def __init__(self,t,f,r,l,b,u):
        self.a=[t,f,r,l,b,u]
        self.direct={'S':(4,0,2,3,5,1),'N':(1,5,2,3,0,4),'E':(3,1,0,5,4,2),'W':(2,1,5,0,4,3)}
    def roll(self,d):
        self.a=[self.a[i] for i in self.direct[d]]
        self.t = self.a[0]
        self.f = self.a[1]
        self.r = self.a[2]
        self.l = self.a[3]
        self.b = self.a[4]
        self.u = self.a[5]
t,f,r,l,b,u=map(int,input().split())
dice=Dice(t,f,r,l,b,u)
for d in input():
    dice.roll(d)
print(dice.t)

