class UnionFind():
  def __init__(self, n=10**6):
    self.n = n
    self.root = [-1]*(n+1)
    self.rnk = [0]*(n+1)
  def find(self, x):
    if(self.root[x] < 0):
      return x
    else:
      self.root[x] = self.find(self.root[x])
      return self.root[x]
  def unite(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if(x == y):return 
    elif(self.rnk[x] > self.rnk[y]):
      self.root[x] += self.root[y]
      self.root[y] = x
    else:
      self.root[y] += self.root[x]
      self.root[x] = y
      if(self.rnk[x] == self.rnk[y]):
        self.rnk[y] += 1
  def same(self, x, y):
    return self.find(x) == self.find(y)
  def count(self, x):
    return -self.root[self.find(x)]
uf=UnionFind()
n=int(input())
for _ in range(n-1):
  u,v,w=map(int,input().split())
  if w%2:
    uf.unite(2*u,2*v-1)
    uf.unite(2*u-1,2*v)
  else:
    uf.unite(2*u,2*v)
    uf.unite(2*u-1,2*v-1)
f=uf.find(2*1)
for i in range(1,n+1):
  print(int(uf.find(2*i)==f))