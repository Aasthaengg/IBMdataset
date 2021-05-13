n,m,k = map(int,input().split())

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

friend = [() for i in range(m)]
uf = UnionFind(n)
for i in range(m):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    uf.union(a, b)
    friend[i] = (a,b)

block = [[]]*k
for i in range(k):
    c,d = map(int,input().split())
    c -= 1
    d -= 1
    block[i] = (c,d)

ans = [uf.size(i) - 1 for i in range(n)]
for i,j in friend:
    if uf.same(i,j):
        ans[i] -= 1
        ans[j] -= 1
for i,j in block:
    if uf.same(i,j):
        ans[i] -= 1
        ans[j] -= 1

print(*ans)