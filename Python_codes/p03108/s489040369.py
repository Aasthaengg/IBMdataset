class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.height = [1] * n
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.height[x] < self.height[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.height[x] == self.height[y]:
                    self.height[x] += 1

    def issame(self, x, y):
        return self.find(x) == self.find(y)

    def group_size(self, x):
        return self.size[self.find(x)]


N, M = map(int, input().split())
int1 = lambda x: int(x) - 1
X = [tuple(map(int1, input().split())) for _ in range(M)]

uf = UnionFind(N)
lst = [0]
for a, b in reversed(X):
    if uf.issame(a, b):
        lst.append(lst[-1])
    else:
        lst.append(lst[-1] + uf.group_size(a) * uf.group_size(b))
    uf.unite(a, b)

for i in range(M - 1, -1, -1):
    print(N * (N - 1) // 2 - lst[i])
