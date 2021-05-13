class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parents[y] = x
            self.size[x] += self.size[y]

N, M = map(int, input().split())
ab = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
uf = UnionFind(N)

now = N*(N-1)//2
ans = [now]
for i in range(M-1):
    a = ab[M - i - 1][0]
    b = ab[M - i - 1][1]
    pa = uf.find(a)
    pb = uf.find(b)
    if pa != pb:
        now -= uf.size[pa] * uf.size[pb]
        uf.union(a, b)
    ans.append(now)
[print(a) for a in ans[::-1]]