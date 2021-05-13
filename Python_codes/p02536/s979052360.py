# union-find
class UnionFind:
    def __init__(self, n):
        self.prsz = [-1] * n # parent & size
    def find(self, v): # root
        if self.prsz[v] < 0: return v
        self.prsz[v] = self.find(self.prsz[v])
        return self.prsz[v]
    def union(self, v, u): # unite
        v = self.find(v); u = self.find(u)
        if v == u: return False
        if self.prsz[v] > self.prsz[u]: v, u = u, v # size(v) < size(u)
        self.prsz[v] += self.prsz[u]
        self.prsz[u] = v
        return True

n, m = map(int, input().split())
uf = UnionFind(n)
for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    uf.union(a, b)
ans = -1
for a in uf.prsz:
    if a < 0: ans += 1
print(ans)
