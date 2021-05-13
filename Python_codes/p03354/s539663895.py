class UnionFind:
    def __init__(self, N):
        self.N = N

        # the parent of all node is itself
        # self.parent = list(range(N))
        self.parent = [-1] * N

    def root(self, i):
        if self.parent[i] < 0:
            return i

        r = self.root(self.parent[i])
        self.parent[i] = r
        return r

    def unite(self, i, j):
        i = self.root(i)
        j = self.root(j)

        if i == j:
            return

        if i > j:
            i, j = j, i

        self.parent[i] += self.parent[j]
        self.parent[j] = i
        # print(self.parent)

    def same(self, i, j):
        return self.root(i) == self.root(j)

    def size(self, i):
        return -self.parent[self.root(i)]

N, M = map(int, input().split())
p = [int(i) - 1 for i in input().split()]

forest = UnionFind(N)

for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    forest.unite(x, y)

ans = 0
for i in range(N):
    if forest.same(i, p[i]):
        ans += 1

print(ans)
