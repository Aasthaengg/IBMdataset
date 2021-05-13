from collections import deque


class UnionFindWeighted:
    """ポテンシャル付きUnionFind"""
    def __init__(self, n):
        self.parent = [-1] * n
        self.weight = [0] * n
        self.cnt = n
        self.INF = 10 ** 18

    def root(self, x):
        """頂点xの根を求める"""
        if self.parent[x] < 0:
            return x
        rt = self.root(self.parent[x])
        self.weight[x] += self.weight[self.parent[x]]
        self.parent[x] = rt
        return rt

    def merge(self, x, y, weight):
        """頂点xを含む集合と頂点y含む集合を結合する
        weight: 頂点yに対する頂点xのポテンシャル(頂点xの方がweight高い)
        """
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return
        if self.parent[root_x] < self.parent[root_y]:
            self.parent[root_x] += self.parent[root_y]
            self.parent[root_y] = root_x
            self.weight[root_y] = -weight + self.weight[x] - self.weight[y]
        else:
            self.parent[root_y] += self.parent[root_x]
            self.parent[root_x] = root_y
            self.weight[root_x] = weight - self.weight[x] + self.weight[y]
        self.cnt -= 1

    def is_same(self, x, y):
        """頂点x, yが同じ集合に属するかどうかを返す"""
        return self.root(x) == self.root(y)

    def diff(self, x, y):
        """頂点yに対する頂点xのポテンシャルを求める
        ただし、頂点x,y間にポテンシャルが定義されていない場合は INF を返す
        """
        if not self.is_same(x, y):
            return self.INF
        return self.weight[x] - self.weight[y]

    def get_size(self, x):
        """頂点xを含む集合の要素数を返す"""
        return -self.parent[self.root(x)]

    def get_cnt(self):
        """集合の個数を返す"""
        return self.cnt


n = int(input())
info = [list(map(int, input().split())) for i in range(n - 1)]
qq, k = map(int, input().split())
query = [list(map(int, input().split())) for i in range(qq)]
k -= 1

tree = [[] for i in range(n)]
for a, b, cost in info:
    a -= 1
    b -= 1
    tree[a].append((b, cost))
    tree[b].append((a, cost))

uf = UnionFindWeighted(n)
root = k
par = {root: -1}
q = deque([root])
while q:
    v = q.pop()
    for nxt_v, cost in tree[v]:
        if nxt_v in par:
            continue
        else:
            par[nxt_v] = v
            uf.merge(nxt_v, par[nxt_v], cost)
            q.append(nxt_v)

for a, b in query:
    a -= 1
    b -= 1
    print(uf.diff(a, k) + uf.diff(b, k))