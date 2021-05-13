n,m=map(int,input().split())
p=list(map(int,input().split()))
class UnionFind(object):
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1 for i in range(N)]
    
    def merge(self, a, b):
        if self.issame(a,b):
            return
        pa = self.root(a)
        pb = self.root(b)
        self.parent[pa] = pb
        self.size[pb] += self.size[pa]
    def root(self, x):
        p = self.parent[x]
        if p == x:
            return x
        else:
            r = self.root(p)
            self.parent[x] = r
            return r
    
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    def getsize(self, x):
        return self.size[self.root(x)]

uf=UnionFind(2*n)
for i in range(n):
    uf.merge(i,p[i]+n-1)
for i in range(m):
    x,y=map(int,input().split())
    x-=1;y-=1
    uf.merge(x,y)
ans=0
for i in range(n):
    ans+=int(uf.issame(i,i+n))
print(ans)