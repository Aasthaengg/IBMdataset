import sys
input = sys.stdin.readline
N, M = map(int, input().split())
qs = []
for _ in range(M):
  u, v = map(int, input().split())
  qs.append((u, v))
qs.reverse()
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.root = [-1] * (n + 1)
    self.rnk = [0] * (n + 1)

  def Find_Root(self, x):
    if self.root[x] < 0:
      return x
    else:
      self.root[x] = self.Find_Root(self.root[x])
      return self.root[x]

  def Unite(self, x, y):
    x = self.Find_Root(x)
    y = self.Find_Root(y)
    if x == y:
      return 
    elif self.rnk[x] > self.rnk[y]:
      self.root[x] += self.root[y]
      self.root[y] = x
    else:
      self.root[y] += self.root[x]
      self.root[x] = y
      if self.rnk[x] == self.rnk[y]:
        self.rnk[y] += 1

  def isSameGroup(self, x, y):
    return self.Find_Root(x) == self.Find_Root(y)

  def Count(self, x):
    return -self.root[self.Find_Root(x)]
uf = UnionFind(N)
res = [N * (N - 1) // 2]
for u, v in qs:
  if uf.isSameGroup(u, v):
    res.append(res[-1])
  else:
    res.append(res[-1] - uf.Count(u) * uf.Count(v))
  uf.Unite(u, v)
res.reverse()
for r in res[1: ]: print(r)