class dice():
    def __init__(self,labels):
        self.l=labels

    def zen(self,a,b):
        x1=self.l[0]
        x2=self.l[1]
        x3=self.l[2]
        x4=self.l[3]
        x5=self.l[4]
        x6=self.l[5]
        if (a,b)==(x1,x2) or (a,b)==(x2,x6) or (a,b)==(x6,x5) or (a,b)==(x5,x1):
            print(x3)
        elif (a,b)==(x3,x2) or (a,b)==(x2,x4) or (a,b)==(x4,x5) or (a,b)==(x5,x3):
            print(x6)
        elif (a,b)==(x6,x2) or (a,b)==(x2,x1) or (a,b)==(x1,x5) or (a,b)==(x5,x6):
            print(x4)
        elif (a,b)==(x3,x1) or (a,b)==(x1,x4) or (a,b)==(x4,x6) or (a,b)==(x6,x3):
            print(x2)
        elif (a,b)==(x3,x6) or (a,b)==(x6,x4) or (a,b)==(x4,x1) or (a,b)==(x1,x3):
            print(x5)
        elif (a,b)==(x4,x2) or (a,b)==(x2,x3) or (a,b)==(x3,x5) or (a,b)==(x5,x4):
            print(x1)

dice=dice([int(i) for i in input().split()])
n=int(input())
for i in range(n):
    a,b=map(int,input().split())
    dice.zen(a,b)

