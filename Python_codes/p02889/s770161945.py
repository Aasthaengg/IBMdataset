import sys
input = sys.stdin.readline

class WarshallFloyd:
    def __init__(self,n):
        self.v = n
        self.d = []
        for i in range(n):
            self.d.append([1e100]*n)
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
        return self.d

n,m,l = map(int,input().split())
wf = WarshallFloyd(n)
for i in range(m):
    a,b,c = map(int,input().split())
    wf.path(a-1,b-1,c)
d = wf.build()

wf = WarshallFloyd(n)
for i in range(1,n):
    for j in range(i):
        if d[i][j] <= l:
            wf.path(i,j,1)

ans = wf.build()

q = int(input())
for i in range(q):
    s,t = map(int,input().split())
    if ans[s-1][t-1] == 1e100:
        print(-1)
    else:
        print(ans[s-1][t-1] - 1)
