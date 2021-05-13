class dice:
    def __init__(self):
        self.d = list(map(int, input().split()))
        self.dir = list(input())
        
    def move(self):
        up = [0,1,2,3] 
        for a in self.dir:
            if a == "E":
                up = [0, 7-up[3], up[2], up[1]]
            elif a == "W":
                up = [0, up[3], up[2], 7-up[1]]
            elif a == "N":
                up = [0, up[2], 7-up[1], up[3]]
            else:
                up = [0, 7-up[2], up[1], up[3]]
        print(self.d[up[1]-1])
ob = dice()
ob.move()

