a = [int(i) for i in input().split()]
dir = input()

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

    #確認用
    def output(self):
        print(self.dise[0])

dise = Dise(a)
dise.roll(dir)
dise.output()

