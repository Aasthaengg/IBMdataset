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

D = Dice(input().split())
for i in input():
    D.rotate(i)
print(D.u)
