N, M = map(int, input().split())
P = list(map(int, input().split()))

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

unionfind = UnionFind(N + 1)

for _ in range(M):
    x, y = map(int, input().split())
    unionfind.union(P[x - 1], P[y - 1])

ans = 0
idx = []
for i in range(N):
    if P[i] == (i + 1):
        ans += 1
    else:
        idx.append(i)
for i in idx:
    if unionfind.same(P[i], i + 1):
        ans += 1
print(ans)