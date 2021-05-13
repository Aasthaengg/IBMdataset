import itertools
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
        return self.d

n,m,l = map(int,input().split())
wf = WarshallFloyd(n)
for i in range(m):
    a,b,c = map(int,input().split())
    wf.path(a-1,b-1,c)
d = wf.build()
tank = WarshallFloyd(n)
for i,j in itertools.combinations(range(n),2):
    if d[i][j] <= l:
        tank.path(i,j,1)
d = tank.build()
q = int(input())
ans = [0]*q
for i in range(q):
    s,t = map(int,input().split())
    ans[i] = d[s-1][t-1] - 1 if d[s-1][t-1] != 1e100 else -1
print('\n'.join(str(i) for i in ans))
