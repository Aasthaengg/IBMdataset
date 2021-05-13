class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)] #親
        self.rank = [0 for _ in range(n)] #根の深さ

    #xの属する木の根を求める
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    #xとyの属する集合のマージ
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    #xとyが同じ集合に属するかを判定
    def same(self, x, y):
        return self.find(x) == self.find(y)

N, M = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(M)]

uf = UnionFind(N)
for i in range(M):
    uf.unite(L[i][0]-1, L[i][1]-1)

team = {}
for i in range(N):
    tmp = uf.find(i)
    if tmp not in team:
        team[tmp] = 1
    else:
        team[tmp] += 1

ans = 0
for k, v in team.items():
    ans = max(ans, v)

print(ans)


