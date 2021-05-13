import itertools 

N,M,R = map(int,input().split())
r = list(map(int,input().split()))

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
wf = WarshallFloyd(N)

for i in range(M):
    a,b,c = map(int,input().split())
    wf.path(a-1,b-1,c)

d = wf.build()
ans = 1e100
for T in itertools.permutations(r):
    Td = 0
    for i in range(len(T) - 1):
        Td += d[T[i]-1][T[i+1] - 1]
    ans = min(ans , Td)
print(ans)
