#UnionFind木
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

  def same(self, x, y):
        return self.find(x) == self.find(y)

  def roots(self):
    return [i for i, x in enumerate(self.parents) if x < 0]

  def members(self, x):
    root = self.find(x)
    return [i for i in range(self.n) if self.find(i) == root]

  def __str__(self):
    return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, M = map(int, input().split())

A = [0]*M
B = [0]*M
for i in range(M):
  A[i],B[i] = map(int, input().split())
  A[i] -= 1
  B[i] -= 1

ans = []

A = A[::-1]
B = B[::-1]
uf = UnionFind(N)
total = N*(N-1)//2
ans.append(total)
for i in range(M):
  if uf.same(A[i],B[i]):
    ans.append(total)
    continue
  m = abs(uf.parents[uf.find(A[i])])
  n = abs(uf.parents[uf.find(B[i])])
  #print(uf)
  #print(A[i]+1,m,B[i]+1,n)
  uf.union(A[i],B[i])
  total -= m*n
  ans.append(total)
  
#print(ans)   

print(*ans[:-1][::-1], sep='\n')
