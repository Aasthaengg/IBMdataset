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

n, m = map(int, input().split())
uf = UnionFind(n)
ans = n*(n-1)/2
l = [ans]
ab = []
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ab.append([a, b])

for a, b in ab[::-1]:
    if uf.same(a, b):
        pass
    else:
        ans -= uf.size(a) * uf.size(b)
    uf.union(a, b)
    l.append(ans)
l.pop()
for i in l[::-1]:
    print(int(i))

