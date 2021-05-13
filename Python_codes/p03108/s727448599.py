n, m = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(m)]

class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1] * (n)
    def find_root(self, x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x
    def merge(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        sx,sy = self.size[x],self.size[y]
        if sx < sy:
            self.root[x] = y
            self.size[y] += sx
        else:
            self.root[y] = x
            self.size[x] += sy
    def same(self, x, y):
        return self.find_root(x) == self.find_root(y)

uf = UnionFind(n)
p = n * (n-1) // 2
ans = [p]
for ai, bi in reversed(ab):
    a_root = uf.find_root(ai-1)
    b_root = uf.find_root(bi-1)
    if a_root != b_root:
        a_size = uf.size[uf.find_root(ai-1)]
        b_size = uf.size[uf.find_root(bi-1)]
        p = p - a_size * b_size
        ans.append(p)
    else:
        ans.append(p)
    uf.merge(ai-1, bi-1)

print('\n'.join(map(str, reversed(ans[:-1]))))
