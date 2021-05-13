NN = 202020
MOD = 10**9+7
INF = float("inf")


class UnionFind2:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def unite(self, x, y):
        if self.same(x, y):
            return
        else:
            parx, pary = self.find(x), self.find(y)
            self.size[pary] += self.size[parx]
            self.size[parx] = 0
            self.par[parx] = pary

    def size(self, x):
        return self.size[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)


n, m = map(int, input().split())
A = list(map(int, input().split()))
S = [list(map(int, input().split())) for i in range(m)]

T = UnionFind2(n)

for i in range(m):
    T.unite(S[i][0]-1, S[i][1]-1)

print(sum([T.same(i, A[i]-1) for i in range(n)]))
