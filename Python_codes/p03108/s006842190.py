import sys
input = sys.stdin.readline
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.root = [-1]*(n+1)
    self.rnk = [0]*(n+1)
  def Find_Root(self, x):
    if(self.root[x] < 0):
      return x
    else:
      self.root[x] = self.Find_Root(self.root[x])
      return self.root[x]
  def Unite(self, x, y):
    x = self.Find_Root(x)
    y = self.Find_Root(y)
    if(x == y):
      return 
    if self.root[x] > self.root[y]:
      x, y = y, x
    self.root[x] += self.root[y]
    self.root[y] = x 
  def isSameGroup(self, x, y):
    return self.Find_Root(x) == self.Find_Root(y)
  def Count(self, x): # xが属するグループのサイズを返す
    return -self.root[self.Find_Root(x)]
  def Members(self, x): # xが属するグループに属する要素をリストで返す
    return [i for i in range(self.n) if self.Find_Root(i)==self.Find_Root(x)]
  def Roots(self): # 全ての根の要素をリストで返す
    return [i for i, x in enumerate(self.root) if x < 0]
  def Group_Count(self): # グループの数を返す
    return len(self.Roots())

N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
uf = UnionFind(N+1)
root_cnt = {i:1 for i in range(1, N+1)}
pair = N*(N-1)//2
ans = []
for i in range(M-1, -1, -1):
  ans += [pair]
  a, b = ab[i]
  ra = uf.Find_Root(a)
  rb = uf.Find_Root(b)
  if uf.isSameGroup(a, b):
    continue
  pair -= root_cnt[ra] * root_cnt[rb]
  uf.Unite(a, b)
  if root_cnt[ra] == root_cnt[uf.Find_Root(a)]:
    root_cnt[ra] += root_cnt[rb]
    root_cnt[rb] = 0
  else:
    root_cnt[rb] += root_cnt[ra]
    root_cnt[ra] = 0
  #root_cnt[uf.Find_Root(a)] += mem_a + mem_b - 1

for n in ans[::-1]:
  print(max(n, 0))