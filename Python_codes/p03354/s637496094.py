# ABC097 D - Equals
class UnionFind:
    # 最初は全てを根として初期化
    def __init__(self, n):
        self.par = [i for i in range(n)]
    
    # データxが属する木の根を再帰で取得する：root(x) = {xの木の根}
    def root(self, x):
        if (self.par[x] == x):
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]
    
    # xとyの木を併合する
    def unite(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry:
            return
        if x < y:
            self.par[ry] = rx
        else:
            self.par[rx] = ry
    # 2つのデータx, yが属する木が同じならtrueを返す
    def same(self, x, y):
        return self.root(x) == self.root(y)

n,m = map(int, input().split())
p = [int(x)-1 for x in input().split()]

ans = 0
UF = UnionFind(n)

for _ in range(m):
    x, y = map(int, input().split())
    UF.unite(x - 1, y - 1)

for i in range(n):
    if UF.same(i,p[i]):
        ans += 1
print(ans)