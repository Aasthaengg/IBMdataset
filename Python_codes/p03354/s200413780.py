class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = list(range(n))
        self.rank = [1]*n
        
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
        
    def unit(self,x,y):
        x, y = self.find(x), self.find(y)
        if x==y: return
        if self.rank[x] < self.rank[y]:
            x,y = y,x
        self.rank[x] += self.rank[y]
        self.par[y] = x
        
n,m,*pxy = map(int,open(0).read().split())
p = pxy[:n]
xy = pxy[n:]

uf = UnionFind(n)

for x,y in zip(xy[::2],xy[1::2]):
    uf.unit(x-1,y-1)

ans = 0
for i,pi in enumerate(p):
    if uf.find(i) == uf.find(pi-1): ans += 1

print(ans)