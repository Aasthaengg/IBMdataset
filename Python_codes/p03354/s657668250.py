class UnionFind:
    def __init__(self, n): # 初期化。1スタートで設計
        self.par = [i for i in range(n+1)] #親
        self.rank = [0]*(n+1) # 高さ

    # 検索
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    # 併合
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)

    # 全ての親の検索（一括での経路圧縮）
    def all_find(self):
        for n in range(len(self.par)):
            self.find(n)

n,m = map(int, input().split())
p = list(map(int, input().split()))
pab = [list(map(int, input().split())) for i in range(m)]

uf = UnionFind(n)
for x,y in pab:
    uf.union(x,y)

uf.all_find()

cnt = 0
for i,k in enumerate(p):
    if k == i+1: # そもそもカウントできる場所にいる場合
        cnt += 1
    else:
        if uf.same_check(i+1,k):
            cnt += 1
print(cnt)
