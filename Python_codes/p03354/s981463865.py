class UnionFind:
    # 初期化
    def __init__(self, n_nodes):
        # 親要素のノード番号を格納する.
        # self.parent[x] == x の時，そのノードは根.
        self.parent = [i for i in range(n_nodes)]

        # 木の高さを格納する．
        self.rank = [0] * n_nodes

    # 検索. 根を返す.
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            # 一度調べた値は，根に繋ぎ直す.
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    # 併合.
    # 木の高さが低くなるように.
    # 親要素の書き換えは少ない方がいい
    def unite(self, x, y):
        # 根を探す．
        x = self.find(x)
        y = self.find(y)

        # 根が同じ場合はそのまま
        if x == y:
            return

        # 木の高さを比較し，低い方を高い方の根に貼る.
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    # 同じ集合に属するか判定
    def check(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int, input().split())
p = list(map(int, input().split()))

tree = UnionFind(N)

for _ in range(M):
    x, y = map(int, input().split())
    tree.unite(x - 1, y - 1)

ans = 0
for i in range(N):
    if tree.check(i, p[i] - 1):
        ans += 1

print(ans)
