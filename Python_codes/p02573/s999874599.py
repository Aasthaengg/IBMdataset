n,m = map(int,input().split())
class dsu:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.sz = [1] * n
    def find(self,a):
        if self.par[a] == a:
            return a
        self.par[a] = self.find(self.par[a])
        return self.par[a]
    def unite(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.sz[b] > self.sz[a]:
                a,b = b,a
            self.par[b] = a
            self.sz[a] += self.sz[b]
d = dsu(n)            
for i in range(m):
    u,v = map(int,input().split())
    d.unite(u-1,v-1)
    
print(max(d.sz) if m else 1)