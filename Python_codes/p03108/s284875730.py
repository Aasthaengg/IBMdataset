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

n,m = map(int,input().split())
uf = UnionFind(n)

A = [0]*m
B = [0]*m

for i in range(m):
  a,b = map(int,input().split())
  A[i],B[i] = a-1, b-1

total = n*(n-1)//2  
ans = [total] 
cost = 0

for a,b in zip(A[::-1],B[::-1]):    
  if uf.same(a,b):
    ans.append(ans[-1])
  else:
    ans.append(ans[-1] - uf.size(a)*uf.size(b))
      
  uf.union(a,b)

ans.pop()
for a in ans[::-1]:
  print(a)