import numpy

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
        # print('root {}, {} = '.format(i, j), end='')
        i = self.root(i)
        j = self.root(j)
        # print(i, j)

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
R = numpy.array([[int(r) for r in input().split()] for _ in range(M)]) - 1

forest = UnionFind(N)
for p1, p2 in R:
    forest.unite(p1, p2)

s = [forest.size(i) for i in range(N)]
print(max(s))