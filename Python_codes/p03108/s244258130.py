#UnionFind木
class UnionFind():
  def __init__(self, n):
    self.n = n
    self.parents = [-1] * n
    #parents属性は根でない場合は自分の親の番号だが、
    #根の場合は負の数で、絶対値がグループのメンバ数を表す

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

  def same(self, x, y):
    return self.find(x) == self.find(y)

  def nums(self,x):
    return abs(self.parents[self.find(x)])

N, M = map(int, input().split())

A = [0]*M
B = [0]*M
for i in range(M-1,-1,-1):
  A[i],B[i] = map(int, input().split())
  A[i] -= 1
  B[i] -= 1

uf = UnionFind(N)
total = N*(N-1)//2
ans = [total]

for i in range(M):
  if uf.same(A[i],B[i]):
    ans.append(total)
    continue
  total -= uf.nums(A[i])*uf.nums(B[i])
  uf.union(A[i],B[i])
  ans.append(total)
  
#print(ans)   
print(*ans[-2::-1], sep='\n')
