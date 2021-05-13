class UnionFind():
  def __init__(self, N):
    self.par = [i for i in range(N)]
 
  def root(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.root(self.par[x])
      return self.par[x]
  
  def unite(self, x, y):
    self.par[self.root(y)] = self.root(x)
    
  def same(self, x, y):
    return self.root(x) == self.root(y)

N, M = map(int, input().split())
p = list(map(int, input().split()))
uf = UnionFind(N)

for i in range(M):
  x, y = map(int, input().split())
  uf.unite(x-1, y-1)
  
r = 0
for i in range(N):
  r += uf.same(i, p[i] - 1)
print(r)
