# import sys
# input = sys.stdin.readline()
n,m = map(int, input().split())
ab = []
for i in range(m):
  a,b = map(int, input().split())
  ab.append([a,b])

class UnionFind:
  def __init__(self,N):
    self.parent = [i for i in range(N)]
    self._size = [1] * N
    self.count = 0
  def root(self,a):
    if self.parent[a] == a:
      return a
    else:
      self.parent[a] = self.root(self.parent[a])
      return self.parent[a]
  def is_same(self,a,b):
    return self.root(a) == self.root(b)
  def unite(self,a,b):
    ra = self.root(a)
    rb = self.root(b)
    if ra == rb: return
    if self._size[ra] < self._size[rb]: ra,rb = rb,ra
    self._size[ra] += self._size[rb]
    self.parent[rb] = ra
    self.count += 1
  def size(self,a):
    return self._size[self.root(a)]


uf = UnionFind(n)

for i in range(m):
  a, b = ab[i][0],ab[i][1]
  a -= 1
  b -= 1
  if uf.is_same(a,b):
    continue
  uf.unite(a,b)
x = 0
for i in range(n):
  x = max(x, uf._size[i])
print (x)