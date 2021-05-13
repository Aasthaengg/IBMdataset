# coding: utf-8

n, m = list(map(int, input().split(" ")))

class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def root(self, n):
        if self.parent[n] == n:
            return n
        else:
            self.parent[n] = self.root(self.parent[n])
            return self.parent[n]

    def union(self, x, y):
        x_root = self.root(x)
        y_root = self.root(y)
        if x_root == y_root:
            pass
        else:
            self.parent[x_root] = y_root

    def same(self, x, y):
        return self.root(x) == self.root(y)

ans = 0

input_ = []
for _ in range(m):
    a, b = list(map(int, input().split(" ")))
    a -= 1
    b -= 1
    input_.append((a, b))

for i in range(m):
    uf = UnionFind(n)
    for j in range(m):
        if i == j:
            continue
        a, b = input_[j]
        uf.union(a, b)
    for k in range(1, n):
        if not uf.same(0, k):
            ans += 1
            break
print(ans)
