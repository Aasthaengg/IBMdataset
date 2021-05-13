F = [int(n) for n in input().split()]
N = int(input())

class Dice():

    def __init__(self,faces):
        self.top = faces[0]
        self.south = faces[1]
        self.east = faces[2]
        self.west = faces[3]
        self.north = faces[4]
        self.bottom = faces[5]

    def rotate(self,d):
        if d == "N":
            tmp = self.top
            self.top = self.south
            self.south = self.bottom
            self.bottom = self.north
            self.north = tmp

        elif d == "S":
            tmp = self.top
            self.top = self.north
            self.north = self.bottom
            self.bottom = self.south
            self.south = tmp

        elif d == "E":
            tmp = self.top
            self.top = self.west
            self.west = self.bottom
            self.bottom = self.east
            self.east = tmp

        elif d == "W":
            tmp = self.top
            self.top = self.east
            self.east = self.bottom
            self.bottom = self.west
            self.west = tmp



    def setTop(self,top):
        if self.south == top:
            self.rotate("N")
        elif self.east == top:
            self.rotate("W")
        elif self.west == top:
            self.rotate("E")
        elif self.north == top:
            self.rotate("S")
        elif self.bottom == top:
            self.rotate("N")
            self.rotate("N")
        

    def setFront(self,front):
        if self.south == front:
            return self.east
        elif self.east == front:
            return self.north
        elif self.west == front:
            return self.south
        elif self.north == front:
            return self.west

    def get_top_value(self):
        return self.top



D = Dice(F)
# for d in D:
#     N.rotate(d)


for _ in range(N):
    top,front = map(int,input().split())
    D.setTop(top)
    print(D.setFront(front))
