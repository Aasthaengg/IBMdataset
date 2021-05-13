class UnionFind():
    def __init__(self, n):
        self.parents = [-1]*n
        self.rank = [0]*n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            return self.find(self.parents[x])

    def size(self, x):
        return -self.parents[self.find(x)]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1


N, M = list(map(int, input().split()))
L = [None]*M
for j in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    L[j] = (a, b)
L = L[::-1]

ans = [0]*(M+1)
ans[0] = (N*(N-1))//2
uf = UnionFind(N)

for j in range(M):
    a, b = L[j]
    if uf.find(a) == uf.find(b):
        ans[j+1] = ans[j]
    else:
        va = uf.size(a)
        vb = uf.size(b)
        ans[j+1] = ans[j]-va*vb
    uf.union(a, b)
# print(ans)
ans = ans[::-1]
for j in range(1, M+1):
    print(ans[j])
