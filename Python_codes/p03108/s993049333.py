n,m = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(m)]
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

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
      
uf = UnionFind(n)
s = n*(n-1)//2
ans = [0]*m
for i in range(m-1,-1,-1):
  if uf.find(ab[i][0]-1) != uf.find(ab[i][1]-1):
    s -= uf.size(ab[i][0]-1)*uf.size(ab[i][1]-1)
  uf.union(ab[i][0]-1,ab[i][1]-1)
  ans[i-1] = s
ans[m-1] = n*(n-1)//2
for i in ans:
  print(i)