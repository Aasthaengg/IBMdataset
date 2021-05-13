class UnionFind():
  def __init__(self, n):
    self.n = n
    self.root = [-1] * (n+1)
    self.rank = [0] * (n+1)
  
  def find(self, x):
    if self.root[x] < 0:
      return x
    else:
      self.root[x] = self.find(self.root[x])
      return self.root[x]
  
  def unite(self, x, y):
    xr = self.find(x)
    yr = self.find(y)
    if xr == yr:
      return
    elif self.rank[xr] < self.rank[yr]:
      self.root[yr] += self.root[xr]
      self.root[xr] = yr
    else:
      self.root[xr] += self.root[yr]
      self.root[yr] = xr
      if self.rank[xr] == self.rank[yr]:
        self.rank[xr] += 1
   
  def same(self, x, y):
    return self.find(x) == self.find(y)
  
  def count(self, x):
    return -self.root[self.find(x)]

N, K, L = map(int, input().split())
roads = UnionFind(N)
for _ in range(K):
  x, y = map(int, input().split())
  roads.unite(x, y)
rails = UnionFind(N)
for _ in range(L):
  x, y = map(int, input().split())
  rails.unite(x, y)
r_dict = {}
for i in range(1, N+1):
  x, y = roads.find(i), rails.find(i)
  if (x, y) in r_dict:
    r_dict[(x, y)] += 1
  else:
    r_dict[(x, y)] = 1
ans = []
for i in range(1, N+1):
  x, y = roads.find(i), rails.find(i)
  ans.append(r_dict[(x, y)])
print(' '.join(map(str, ans)))