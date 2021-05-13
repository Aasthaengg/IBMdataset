N, M = map(int, input().split())
nums = list(map(int, input().split()))
ids = [0] * (N+1)
for i, n in enumerate(nums):
  ids[n] = i+1

class UnionFind():
  
  def __init__(self, n):
    self.par = list(range(n+1))
    self.rank = [0] * (n+1)

  def root(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.root(self.par[x])
      return self.par[x]

  def unite(self, x, y):
    xr = self.root(x)
    yr = self.root(y)
    if xr == yr:
      return
    if self.rank[xr] < self.rank[y]:
      self.par[xr] = yr
    else:
      self.par[yr] = xr
      if self.rank[xr] == self.rank[y]:
        self.rank[xr] += 1

  def same(self, x, y):
    return self.root(x) == self.root(y)

i_tree = UnionFind(N)
  
for _ in range(M):
  x, y = map(int, input().split())
  i_tree.unite(x, y)
cnt = 0
for i in range(1, N+1):
  if i_tree.same(i, ids[i]):
    cnt += 1
print(cnt)