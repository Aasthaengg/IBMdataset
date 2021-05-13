a = [int(i) for i in input().split()]
n = int(input())

class Dise:
    def __init__(self,a):
        self.dise = [0 for i in range(len(a))]
        for i in range(len(a)):
            self.dise[i] = a[i]

    def roll(self,dir):
        for self.pop_str in dir:
            if self.pop_str == "N":
                self.dise[0],self.dise[1],self.dise[4],self.dise[5] = self.dise[1],self.dise[5],self.dise[0],self.dise[4]
            elif self.pop_str == "S":
                self.dise[0],self.dise[1],self.dise[4],self.dise[5] = self.dise[4],self.dise[0],self.dise[5],self.dise[1]
            elif self.pop_str == "E":
                self.dise[0],self.dise[2],self.dise[3],self.dise[5] = self.dise[3],self.dise[0],self.dise[5],self.dise[2]
            elif self.pop_str == "W":
                self.dise[0],self.dise[2],self.dise[3],self.dise[5] = self.dise[2],self.dise[5],self.dise[0],self.dise[3]

    def N(self):
        self.dise[0],self.dise[1],self.dise[4],self.dise[5] = self.dise[1],self.dise[5],self.dise[0],self.dise[4]

    def S(self):
        self.dise[0],self.dise[1],self.dise[4],self.dise[5] = self.dise[4],self.dise[0],self.dise[5],self.dise[1]

    def E(self):
        self.dise[0],self.dise[2],self.dise[3],self.dise[5] = self.dise[3],self.dise[0],self.dise[5],self.dise[2]

    def W(self):
        self.dise[0],self.dise[2],self.dise[3],self.dise[5] = self.dise[2],self.dise[5],self.dise[0],self.dise[3]

    def R(self):
        self.dise[1],self.dise[2],self.dise[3],self.dise[4] = self.dise[3],self.dise[1],self.dise[4],self.dise[2]

    def L(self):
        self.dise[1],self.dise[2],self.dise[3],self.dise[4] = self.dise[2],self.dise[4],self.dise[1],self.dise[3]

    #確認用
    def output(self):
        print(self.dise[2])


for i in range(n):
    X = Dise(a)
    count = 0
    top,front = [int(i) for i in input().split()]

    while X.dise[0] != top and X.dise[1] != front:
        X.N()
        count += 1
        if count >= 4:
            X.E()
            count += 1
            if count >= 8:
                X.R()

    if X.dise[0] == top:
        while X.dise[1] != front:
            X.R()
    elif X.dise[1] == front:
        while X.dise[0] != top:
            X.E()
    X.output()

