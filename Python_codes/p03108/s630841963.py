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
      return False,0,0

    if self.parents[x] > self.parents[y]:
      x, y = y, x
    nx=self.size(x)
    ny=self.size(y)
    self.parents[x] += self.parents[y]
    self.parents[y] = x
    
    return True,nx,ny

  def size(self, x):
    return -self.parents[self.find(x)]

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]

  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]
    
  def all_group_numbers(self):
    return [-x for x in self.parents if x < -1]

  def group_count(self):
    return len(self.roots())

  def all_group_members(self):
    return {r: self.members(r) for r in self.roots()}

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
N,M=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(M)]
uf=UnionFind(N)
ans=[0]*(M+1)
ans[M]=N*(N-1)//2
i=M-1
for a,b in AB[::-1]:
  flg,na,nb=uf.union(a-1,b-1)
  if flg:
    ans[i]=ans[i+1]-na*nb
  else:
    ans[i]=ans[i+1]
  i-=1
for a in ans[1:]:
  print(a)

