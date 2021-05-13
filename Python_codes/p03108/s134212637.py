n,m=map(int,input().split())
ab=[list(map(int,input().split())) for _ in range(m)]
ab=[[a-1,b-1] for a,b in ab]
# Union FInd
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
ans=[]
ans.append((n*(n-1))//2)
uf=UnionFind(n)
ab.reverse()
for a,b in ab:
  if uf.same(a,b):
    ans.append(ans[-1])
  else:
    x1=uf.size(a)
    x2=uf.size(b)
    ans.append(ans[-1]-x1*x2)
    uf.union(a,b)
ans.reverse()
for ai in ans[1:]:
  print(ai)