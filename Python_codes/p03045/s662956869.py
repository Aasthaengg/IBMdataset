N, M = map(int, input().split())

class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)

    if x == y:
      return

    if self.parents[x] > self.parents[y]:
            x, y = y, x

    self.parents[x] += self.parents[y]
    self.parents[y] = x

  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]

uf = UnionFind(N)

for _ in range(M):
  x,y,z = map(int, input().split())
  uf.union(x-1,y-1)
  
ans = len(uf.roots())
  
print(ans)