n , m = map(int, input().split())
bridge = []
for i in range(m):
    a , b = map(int, input().split())
    bridge.append((a,b))

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

uf = UnionFind(n)
ans1 = n*(n-1)//2
ans = []
for i in range(m):
    ans.append(ans1)
    a1,b1=bridge[m-1-i]
    a1-=1
    b1-=1
    if not uf.same(a1,b1):
        ans1 -= uf.size(a1)*uf.size(b1)
    uf.union(a1,b1)

ans.reverse()
for i in ans:
    print(i)
