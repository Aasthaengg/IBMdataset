import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


class UnionFind:
    def __init__(self, n):
        self.p = [-1]*n
        self.r = [1]*n

    def find(self, x):
        if self.p[x] < 0:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.r[rx] > self.r[ry]:
                rx, ry = ry, rx
            if self.r[rx] == self.r[ry]:
                self.r[ry] += 1
            self.p[ry] += self.p[rx]
            self.p[rx] = ry

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.p[self.find(x)]


n, m = map(int, input().split())
uf = UnionFind(n)
edges = [tuple(map(lambda x: int(x)-1, input().split()))for _ in range(m)]


ans_inv = [n*(n-1)//2]
for a, b in reversed(edges):
    if uf.same(a, b):
        ans = ans_inv[-1]
    else:
        x = uf.size(a)
        y = uf.size(b)
        ans = ans_inv[-1]-x*y
    ans_inv.append(ans)
    uf.union(a, b)

print(*reversed(ans_inv[:-1]), sep='\n')