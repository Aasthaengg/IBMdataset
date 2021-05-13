class DisjointSet:
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
brg = [[int(i)-1 for i in input().split()] for _ in range(m)]
cnt = n*(n-1)//2
ans = [0]*m
ds = DisjointSet(n)
for i in range(m)[::-1]:
    ans[i] = cnt
    a,b = brg[i]
    if not ds.same(a,b):
        cnt -= ds.size(a)*ds.size(b)
        ds.unite(a,b)
print("\n".join(map(str,ans)))