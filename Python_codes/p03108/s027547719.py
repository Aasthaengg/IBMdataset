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

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())

N, M = list(map(int, input().split()))
edges = [list(map(int, input().split())) for i in range(M)]


uni = UnionFind(N)
res = []
for a,b in edges[::-1]:
    if uni.find(a-1) != uni.find(b-1):
        siz_a = uni.size(a-1)
        siz_b = uni.size(b-1)
        tmp = siz_a * siz_b
        res.append(tmp)
    else:
        res.append(0)
    uni.union(a-1, b-1)

bef = 0
for v in res[::-1]:
    print(v+bef)
    bef += v 