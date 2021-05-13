class UnionFind(object):
    def __init__(self, n=1):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = [1 for _ in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                x, y = y, x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
            self.par[y] = x
            self.size[x] += self.size[y]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    def get_size(self, x):
        x = self.find(x)
        return self.size[x]
    
n,m=map(int,input().split())
uf1=UnionFind(n)
ab=[]
res=[]
for i in range(m):
    a,b=map(int,input().split())
    a,b=a-1,b-1
    ab.append((a,b))
for a,b in ab[::-1]:
    aa=uf1.find(a)
    bb=uf1.find(b)
    if aa==bb:
        res.append(0)
    else:
        res.append(uf1.get_size(aa)*uf1.get_size(bb))
        uf1.union(aa,bb)
ans=0
for i in range(m):
    ans+=res[m-1-i]
    print(ans)