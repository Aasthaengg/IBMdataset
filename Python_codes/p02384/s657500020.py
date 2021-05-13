class Dice:
    def __init__(self,label):
        self.W = label[3]
        self.S = label[1]
        self.E = label[2]
        self.N = label[4]
        self.u = label[0]
        self.l = label[5]
    def rotate(self,direction):
        if direction =='S':
            dummy = self.S
            self.S = self.u
            self.u = self.N
            self.N = self.l
            self.l = dummy
        elif direction == 'N':
            dummy = self.S
            self.S = self.l
            self.l = self.N
            self.N = self.u
            self.u = dummy
        elif direction == 'W':
            dummy = self.W
            self.W = self.u
            self.u = self.E
            self.E = self.l
            self.l = dummy
        else:
            dummy = self.W
            self.W = self.l
            self.l = self.E
            self.E = self.u
            self.u = dummy
    def rot(self):
            dummy = self.W
            self.W = self.S
            self.S = self.E
            self.E = self.N
            self.N = dummy

l = input().split()
D = Dice(l)
n = int(input())
for i in range(n):
    a,b = input().split()
    if a == D.u:
        c = 1
    elif a == D.N:
        D.rotate('S')
    elif a == D.W:
        D.rotate('E')
    elif a == D.E:
        D.rotate('W')
    elif a == D.S:
        D.rotate('N')
    else:
        D.rotate('S')
        D.rotate('S')
    for i in range(4):
        D.rot()
        if (D.S == b)+(D.S == str(b)):
            break
    print(D.E)
    D = Dice(l)
    
