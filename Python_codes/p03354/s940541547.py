class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def find(self, x):
        if self.parents[x] == x:
            return x
        ret = self.parents[x] = self.find(self.parents[x])
        return ret

    def is_family(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return False
        self.parents[root_x] = root_y
        return True


n, m = [int(i) for i in input().split()]
pp = [int(i)-1 for i in input().split()]
uf = UnionFind(n)
for _ in range(m):
    x, y = [int(i) for i in input().split()]
    uf.union(x-1, y-1)

ans = 0
for i, p in enumerate(pp):
    if uf.is_family(i, p):
        ans += 1

print(ans)
