class DisjointSet:
    def __init__(self,n):
        self.rank = [0]*n
        self.parent = [i for i in range(n)]
        self.siz = [1]*n

    def same(self,x,y): 
        return self.findSet(x) == self.findSet(y)

    def unite(self,x,y): 
        return self.link(self.findSet(x), self.findSet(y))

    def link(self,x,y):
        if self.rank[x] > self.rank[y]: 
            self.parent[y] = x
            self.siz[x] += self.siz[y]
        else:
            self.parent[x] = y
            self.siz[y] += self.siz[x]
            if self.rank[x] == self.rank[y]: self.rank[y] += 1

    def findSet(self,x):
        if x != self.parent[x]: 
            self.parent[x] = self.findSet(self.parent[x])
        return self.parent[x]

    def size(self,x):
        return self.siz[self.findSet(x)]

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