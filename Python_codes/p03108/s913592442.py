N, M = list(map(int,input().split()))
in_ = []
for i in range(M):
    a, b = map(int, input().split())
    in_.append([a, b])

class UnionFind():

    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:  return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:  return

        if self.parents[x] > self.parents[y]:  x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):  return -self.parents[self.find(x)]

    def same(self, x, y):  return self.find(x) == self.find(y)
        
uf = UnionFind(N)
cnt = N * (N - 1) // 2
ans = [0 for _ in range(M)]

for i in range(M):
    ans[-i - 1] = cnt
    a, b = in_[-i - 1][0] - 1, in_[-i - 1][1] - 1
    if uf.same(a, b):  continue
    cnt -= (uf.size(a) * uf.size(b))
    uf.union(a, b)

for i in range(M):  print(ans[i])