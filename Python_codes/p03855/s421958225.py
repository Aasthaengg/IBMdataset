N, K, L = map(int, input().split())

class UnionFind():
  def __init__(self):
    self.par = [i for i in range(N)]

  def root(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.root(self.par[x])
      return self.par[x]
  
  def unite(self, x, y):
    self.par[self.root(y)] = self.root(x)

ufRoad = UnionFind()

for i in range(K):
  p, q = map(int, input().split())
  ufRoad.unite(p-1, q-1)

ufRail = UnionFind()

for i in range(L):
  r, s = map(int, input().split())
  ufRail.unite(r-1, s-1)

d = {}

for i in range(N):
  d[(ufRoad.root(i), ufRail.root(i))] = d.get((ufRoad.root(i), ufRail.root(i)), 0) + 1

r = [0] * N

for i in range(N):
  r[i] = d.get((ufRoad.root(i), ufRail.root(i)))

print(*r)