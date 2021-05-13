class Dice:
    def __init__(self,dim=list(range(1,7))):
        self.dim = dim

    def roll(self,direction):
        if direction == "N":
            buff = self.dim[0]
            self.dim[0] = self.dim[1]
            self.dim[1] = self.dim[5]
            self.dim[5] = self.dim[4]
            self.dim[4] = buff

        if direction == "E":
            buff = self.dim[3]
            self.dim[3] = self.dim[5]
            self.dim[5] = self.dim[2]
            self.dim[2] = self.dim[0]
            self.dim[0] = buff

        if direction == "W":
            buff = self.dim[0]
            self.dim[0] = self.dim[2]
            self.dim[2] = self.dim[5]
            self.dim[5] = self.dim[3]
            self.dim[3] = buff

        if direction == "S":
            buff = self.dim[0]
            self.dim[0] = self.dim[4]
            self.dim[4] = self.dim[5]
            self.dim[5] = self.dim[1]
            self.dim[1] = buff

lst = list(map(int,input().split()))

D = Dice(lst)
code = input()
for i in code:
    D.roll(i)

print(D.dim[0])
