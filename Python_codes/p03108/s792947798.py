class UnionFind(object):
    def __init__(self, n):
        self.par = [-1] * n
    
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return False
        else:
            if self.par[x] > self.par[y]:
                x, y = y, x
            self.par[x] += self.par[y]
            self.par[y] = x
            return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.par) if x < 0]

    def group_count(self):
        return len(self.roots())

N, M = map(int, input().split())
uf = UnionFind(N)

# 最後は全部つながってない
# うしろから順番につなぐ
edges = []
for _ in range(M):
    ai, bi = map(int, input().split())
    ai, bi = ai - 1, bi - 1
    edges.append((ai, bi))
edges.reverse()

ans = [N * (N - 1) // 2]
for (ai, bi) in edges:
    if not uf.same(ai, bi):
        ans.append(ans[-1] - uf.size(ai) * uf.size(bi))
    else:
        ans.append(ans[-1])
    uf.unite(ai, bi)

for a in ans[::-1][1:]:
    print(a)