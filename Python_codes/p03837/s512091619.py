import sys
input = sys.stdin.readline

class WarshallFloyd:
    def __init__(self,n):
        self.v = n
        self.d = [[1e100]*n for _ in range(n)]
        for i in range(n):
            self.d[i][i] = 0

    def path(self,x,y,c):
        if x == y:
            return False
        self.d[x][y] = c
        self.d[y][x] = c
        return True

    def build(self):
        for k in range(self.v):
            for i in range(self.v):
                for j in range(self.v):
                    self.d[i][j] = min(self.d[i][j], self.d[i][k] + self.d[k][j])

n,m = map(int,input().split())
ABC = [tuple() for _ in range(m)]
wf = WarshallFloyd(n)
for i in range(m):
    a,b,c = map(int,input().split())
    wf.path(a-1,b-1,c)
    ABC[i] = (a-1,b-1,c)
ans = 0
wf.build()
for a,b,c in ABC:
    ans += (c > wf.d[a][b])
print(ans)
