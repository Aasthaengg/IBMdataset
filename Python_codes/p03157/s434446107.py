H, W = map(int, input().split())
m = [input() for i in range(H)]
ans = 0

import sys
sys.setrecursionlimit(10**6)

class UnionFind():
  def __init__(self, n):
    self.par = [i for i in range(n)]

  def root(self, x):
    if self.par[x] == x:
      return x
    else:
      self.par[x] = self.root(self.par[x])
      return self.par[x]
  
  def unite(self, x, y):
    x = self.root(x)
    y = self.root(y)
    self.par[y] = x

  def same(self, x, y):
    return self.root(x) == self.root(y)

uf = UnionFind(H*W)

for i in range(H*W):
  h, w = divmod(i, W)
  if 0 <= h-1 and m[h-1][w] != m[h][w]: uf.unite(h*W + w, (h-1)*W + w)
  if h+1 < H  and m[h+1][w] != m[h][w]: uf.unite(h*W + w, (h+1)*W + w)
  if 0 <= w-1 and m[h][w-1] != m[h][w]: uf.unite(h*W + w, h*W + (w-1))
  if w+1 < W  and m[h][w+1] != m[h][w]: uf.unite(h*W + w, h*W + (w+1))

ansb = {}
answ = {}
for i in range(H*W):
  ir = uf.root(i)
  h, w = divmod(i, W)
  if m[h][w] == "#":
    ansb[ir] = ansb.get(ir, 0) + 1
  else:
    answ[ir] = answ.get(ir, 0) + 1


ans = 0
for k, vb in ansb.items():
  vw = answ.get(k, 0)
  ans += vb * vw

print(ans)