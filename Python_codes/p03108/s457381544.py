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
n,m=map(int,input().split())
uf = UnionFind(n)
edges=[]
for i in range(m):
  edges.append(list(map(int,input().split())))
current=(n*(n-1))//2
ans=[current]
for i in range(m-1):
  u=edges[m-1-i][0]-1
  v=edges[m-1-i][1]-1
  if uf.same(u,v)==1:
    ans.append(current)
  else:
    size1=uf.size(u)
    size2=uf.size(v)
    current-=size1*size2
    ans.append(current)
    uf.union(u,v)
ans.reverse()
for i in ans:
  print(i)