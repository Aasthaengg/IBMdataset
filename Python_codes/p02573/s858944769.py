class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1 for i in range(n)]

  def find(self, x):
    if self.parents[x] < 0:
      return x
    else:
      self.parents[x] = self.find(self.parents[x])
      return self.parents[x]
  
  def union(self, x, y):
    x, y = self.find(x), self.find(y)
    if x == y:
      return
    if self.parents[x] > self.parents[y]:
      x, y = y, x
    self.parents[x] += self.parents[y]
    self.parents[y] = x

N, M = map(int, input().split())
friend_lis = [list(map(int, input().split())) for i in range(M)]

lis = UnionFind(N)
for i,j in friend_lis:
  lis.union(i-1, j-1)
#print(lis.parents)

ans = -min(lis.parents)
print(ans)