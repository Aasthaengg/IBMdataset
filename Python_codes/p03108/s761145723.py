class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1]*n
    
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
            x,y = y,x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)
      
    def size(self, x):
        return -self.parents[self.find(x)]

N, M = map(int, input().split())
A = list()
B = list()
for j in range(M):
  a, b = map(int, input().split())
  A.append(a)
  B.append(b)
ans = [0] * M
ans[M-1] = N*(N-1)//2
uf = UnionFind(N+1)
for i in range(M-1, 0, -1):
  a = A[i]
  b = B[i]
  if uf.same(a,b): 
    ans[i-1] = ans[i]
  else:
    ans[i-1] = ans[i] - uf.size(a)*uf.size(b)
  uf.union(a, b)
    
for i in range(M):
  print(ans[i])