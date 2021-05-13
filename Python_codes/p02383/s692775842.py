class dice:
    def __init__(self, pip):
        self.pip = pip
        
    def move(self,dir):
        if str(dir) == "E":
            self.pip[0],self.pip[2],self.pip[3],self.pip[5] = self.pip[3],self.pip[0],self.pip[5],self.pip[2]
        elif str(dir) == "W":
            self.pip[0],self.pip[2],self.pip[3],self.pip[5] = self.pip[2],self.pip[5],self.pip[0],self.pip[3]
        elif str(dir) == "N":
            self.pip[0],self.pip[1],self.pip[4],self.pip[5] = self.pip[1],self.pip[5],self.pip[0],self.pip[4]
        elif str(dir) == "S":
            self.pip[0],self.pip[1],self.pip[4],self.pip[5] = self.pip[4],self.pip[0],self.pip[5],self.pip[1]

d = dice(list(map(int,input().split())))
inp = list(input())

for dir in inp:
    d.move(dir)

print(d.pip[0])

