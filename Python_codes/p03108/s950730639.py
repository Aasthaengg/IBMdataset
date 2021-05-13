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

  def size(self, x):
    return -self.parents[self.find(x)]

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]

  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]

  def group_count(self):
    return len(self.roots())

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
n,m=map(int,input().split())
t=n*(n-1)//2
x=[t]
gr=[]
for i in range(m):
  a,b=map(int,input().split())
  gr.append((a-1,b-1))
gr=gr[::-1]
uf=UnionFind(n)
for a,b in gr:
  if uf.same(a,b)==False:
    t-=(uf.size(a)*uf.size(b))
  x.append(t)
  uf.union(a,b)
x=x[:m]
print(*x[::-1])