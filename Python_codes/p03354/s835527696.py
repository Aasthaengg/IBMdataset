class DisjointSets:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.siz = [1]*n

    def root(self,x):
        if x != self.parent[x]: 
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def same(self,x,y): 
        return self.root(x) == self.root(y)

    def unite(self,x,y): 
        x = self.root(x)
        y = self.root(y)
        if x == y: 
            return
        if self.siz[x] < self.siz[y]: 
            x,y = y,x
        self.parent[y] = x
        self.siz[x] += self.siz[y]

    def size(self,x):
        return self.siz[self.root(x)]

n,m = map(int,input().split())
p = [int(i)-1 for i in input().split()]
ds = DisjointSets(n)
for i in range(m):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    ds.unite(x,y)
ans = 0
for i,p in enumerate(p):
    if ds.same(i,p): ans += 1
print(ans)