class dice:
    def roll(self,direction):
        if direction=="N":
            self.face=[self.face[1],self.face[5],self.face[2],self.face[3],self.face[0],self.face[4]]
        if direction=="E":
            self.face=[self.face[3],self.face[1],self.face[0],self.face[5],self.face[4],self.face[2]]
        if direction=="W":
            self.face=[self.face[2],self.face[1],self.face[5],self.face[0],self.face[4],self.face[3]]
        if direction=="S":
            self.face=[self.face[4],self.face[0],self.face[2],self.face[3],self.face[5],self.face[1]]
dice1=dice()
dice1.face=list(map(int,input().split()))
for i in input():
    dice1.roll(i)
print(dice1.face[0])
