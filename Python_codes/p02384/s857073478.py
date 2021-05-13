class Dice():
    
    def __init__(self,d1,d2,d3,d4,d5,d6):
        self.d1=d1
        self.d2=d2
        self.d3=d3
        self.d4=d4
        self.d5=d5
        self.d6=d6
    
    def roll(self,c):
        if c=='N':
            self.d1,self.d5,self.d6,self.d2=self.d2,self.d1,self.d5,self.d6
        elif c=='S':
            self.d1,self.d5,self.d6,self.d2=self.d5,self.d6,self.d2,self.d1
        elif c=='E':
            self.d1,self.d3,self.d6,self.d4=self.d4,self.d1,self.d3,self.d6
        else:
            self.d1,self.d3,self.d6,self.d4=self.d3,self.d6,self.d4,self.d1
    
a,b,c,d,e,f=map(int,input().split())
D=Dice(a,b,c,d,e,f)
n=int(input())
for i in range(n):
    up,forward=map(int,input().split())
    if up==D.d3:
        D.roll('W')
    elif up==D.d6:
        D.roll('E')
        D.roll('E')
    elif up==D.d4:
        D.roll('E')
    elif up==D.d2:
        D.roll('N')
    elif up==D.d5:
        D.roll('S')
    if forward==D.d2:
        print(D.d3)
    elif forward==D.d3:
        print(D.d5)
    elif forward==D.d5:
        print(D.d4)
    else:
        print(D.d2)
