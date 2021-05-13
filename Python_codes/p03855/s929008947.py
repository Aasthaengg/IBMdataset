n,k,l=map(int,input().split())
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
uf1=UnionFind(n)
uf2=UnionFind(n)
d=dict()
a,b=[0]*n,[0]*n
for i in range(k):
  p,q=map(int,input().split())
  uf1.union(p-1,q-1)
ans=[0]*n
for i in range(l):
  r,s=map(int,input().split())
  uf2.union(r-1,s-1)
for i in range(n):
  a[i]=uf1.find(i)
  b[i]=uf2.find(i)
  if (a[i],b[i]) not in d:
    d[(a[i],b[i])]=1
  else:
    d[(a[i],b[i])]+=1
for i in range(n):
  ans[i]=d[(a[i],b[i])]
print(*ans)