N, M = [int(i) for i in input().split()]
Pn = [int(i) for i in input().split()]
XYm = [[int(i) for i in input().split()] for _ in range(M)]

class UnionFind:
  def __init__(self, N, arr=None):
    if arr is None:
      self.roots = [-1 for i in range(N)]
      self.ranks = [0 for i in range(N)]
    else:
      self.roots = arr[:]
      self.ranks = [0 for i in range(N)]
            
  def root(self, i):
    root = self.roots[i]
    if root < 0:
      return i
    else:
      return self.root(root)
      
  def union(self, i, j):
    x = self.root(i)
    y = self.root(j)
    if x == y:
      return
    if self.ranks[x] < self.ranks[y]:
      self.roots[x] = y
    else:
      self.roots[y] = x
      if self.ranks[x] == self.ranks[y]:
        self.ranks[x] += 1
  
  def same(self, i, j):
    return self.root(i) == self.root(j)
  
  def get_rank(self, i):
    root = self.root(i)
    return self.ranks[root]
  
uf = UnionFind(N)
for xy in XYm:
  x, y = xy
  uf.union(x-1, y-1)
  
count = 0
for i in range(N):
  count += 1 if uf.same(i, Pn[i]-1) else 0
print(count)

