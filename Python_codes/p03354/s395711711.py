class UnionFind:
  def __init__(self, n):
    self.par = [i for i in range(n)]
    self.rank = [0]*n
  def find(self, x):
    if self.par[x]==x:
      return x
    else:
      self.par[x] = self.find(self.par[x])
      return self.par[x]
  def unit(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x==y:
      return
    elif self.rank[x]<self.rank[y]:
      self.par[x] = y
      return
    elif self.rank[y]<self.rank[x]:
      self.par[y] = x
    else:
      self.par[y] = x
      self.rank[x] += 1
      
  def same(self, x, y):
    return self.find(x)==self.find(y)
  

N, M, *L = map(int, open(0).read().split())
p = L[:N]
ls = L[N:]
u = UnionFind(N+1)
for x,y in zip(*[iter(ls)]*2):
  u.unit(x,y)
inf = [0]*(N+1)
for i in range(N):
  inf[p[i]] = i
ans = sum(1 if u.same(i,inf[i]+1) else 0 for i in range(1,N+1))
print(ans)