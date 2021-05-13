class UnionFind():
  def __init__(self, n):
    self.n = n
    self.root = [-1]*(n+1)
    self.rank = [0]*(n+1)
  
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
    elif self.rank[x] > self.rank[y]:
        self.root[x] += self.root[y]
        self.root[y] = x
    else:
        self.root[y] += self.root[x]
        self.root[x] = y
        if self.rank[x] == self.rank[y]:
          self.rank[y] += 1
  def Is_Same_Group(self, x, y):
    return self.Find_Root(x) == self.Find_Root(y)
  
  def Count(self, x):
    return -self.root[self.Find_Root(x)]

n,k,l=map(int,input().split())
douro=UnionFind(n)
tetudou=UnionFind(n)
for i in range(k):
  p,q=map(int,input().split())
  douro.Unite(p-1, q-1)
for i in range(l):
  r,s=map(int,input().split())
  tetudou.Unite(r-1, s-1)

d={}
for i in range(n):
  pair=(douro.Find_Root(i), tetudou.Find_Root(i))
  if pair in d:
    d[pair] += 1
  else:
    d[pair] = 1

print(' '.join([str(d[(douro.Find_Root(i), tetudou.Find_Root(i))]) for i in range(n)]))
