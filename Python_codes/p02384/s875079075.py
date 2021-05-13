class dice:
    def __init__(self):
        self.d = [0] + list(map(int, input().split()))
        
    def move(self):
        dir = list(input())
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
        print(self.d[up[1]])
        
    def solve(self):
        top, front = map(int, input().split())
        T = self.d.index(top)
        F = self.d.index(front)
        L =[[1,2,3], [2,6,3], [6,5,3], [5,1,3], [2,3,1], [3,5,1], [5,4,1], [4,2,1], [1,4,2], [4,6,2], [6,3,2], [3,1,2]]
        for l in L:
            if l[0] == T and l[1] == F:
                print(self.d[l[2]])
                break
            elif l[1] == T and l[0] == F:
                print(self.d[7-l[2]])
                break

ob = dice()
for x in range(int(input())):
    ob.solve()
        
        


