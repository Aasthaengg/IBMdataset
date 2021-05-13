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
    def get_group(self):
        a=0
        for i in range(len(self.par)):
          if self.find(i)==i:
            a+=1
        return a
N,M=map(int,input().split())
lity=[]
lity.append(int(N*(N-1)/2))
ans=0
uf=UnionFind(N)
AB=[list(map(int,input().split())) for i in range(M)]
for i in range(M-1,-1,-1):
  a,b=AB[i]
  x=uf.find(a-1)
  y=uf.find(b-1)
  sizex=0
  sizey=0
  if x!=y:
    sizex=uf.get_size(a-1)
    sizey=uf.get_size(b-1)
  uf.union(a-1,b-1)
  ans=lity[-1]-sizex*sizey
  lity.append(ans)
for j in range(M-1,-1,-1):
  print(lity[j])