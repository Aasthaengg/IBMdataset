n,m=map(int,input().split())
ab=[]
for _ in range(m):
  a,b=map(int,input().split())
  a-=1
  b-=1
  ab.append((a,b))
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
uf=UnionFind(n)
ans=[n*(n-1)//2]
for i in range(m):
  a,b=ab[m-i-1]
  if uf.same(a,b):
    ans.append(ans[-1])
  else:
    asize=uf.size(a)
    bsize=uf.size(b)
    ans.append(ans[-1]-asize*bsize)
    uf.union(a,b)
for i in range(m):
  print(ans[m-i-1])