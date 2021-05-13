N,M = map(int, input().strip().split(' '))
P = list(map(int, input().strip().split(' ')))
P = [p-1 for p in P]

class UnionFind:
  def __init__(self, n):
    self.tree = list(range(n))
    
  def root(self, n):
    if self.tree[n] == n:
      return n
    else:
      self.tree[n] = self.root(self.tree[n])
      return self.tree[n]
  
  def marge(self, x, y):
    if not self.root(x) == self.root(y):
      self.tree[self.root(y)] = self.root(x)
  
# グループごとに考えればよい
uf = UnionFind(N)
for _ in range(M):
  x,y = map(int, input().strip().split(' '))
  x,y = x-1,y-1
  uf.marge(x,y)

groups = [set() for _ in range(N)]
for i in range(N):
  groups[uf.root(i)].add(i)

ans = 0
for g in groups:
  if len(g) == 0: continue
  ans += len(set(P[i] for i in g) & g)

print(ans)

