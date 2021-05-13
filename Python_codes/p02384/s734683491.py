
class Dice:
    def __init__(self,a,b,c,d,e,f):
        self.face1 = a
        self.face2 = b
        self.face3 = c
        self.face4 = d
        self.face5 = e
        self.face6 = f

    def above_face(self):
        return self.face1

    def roll(self, order):
        if order == 0:
            tmp = self.face1
            self.face1 = self.face2
            self.face2 = self.face6
            self.face6 = self.face5
            self.face5 = tmp
        elif order == 1:
            tmp = self.face1
            self.face1 = self.face5
            self.face5 = self.face6
            self.face6 = self.face2
            self.face2 = tmp
        elif order == 2:
            tmp = self.face1
            self.face1 = self.face3
            self.face3 = self.face6
            self.face6 = self.face4
            self.face4 = tmp
        else:
            tmp = self.face1
            self.face1 = self.face4
            self.face4 = self.face6
            self.face6 = self.face3
            self.face3 = tmp

a,b,c,d,e,f = map(int,input().split())
dice1 = Dice(a,b,c,d,e,f)
q = int(input())
import random
for i in range(q):
    A,B = map(int,input().split())
    while True:
        dice1.roll(random.randint(0, 3))
        if dice1.face1 == A and dice1.face2 == B:
            break
    print(dice1.face3)

