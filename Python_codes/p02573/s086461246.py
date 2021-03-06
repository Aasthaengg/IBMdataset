# 最大の友達集団の人の数ぶんだけグループに分ける必要がある。
# union-findを使用する必要がある。

class UnionFind:
    # この時点でそれぞれのノードは自分を親としている
    # 初期化時に問題が0の頂点を認めるかに注意すること
    def __init__(self, n):
        self.N = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    # xの根を返す関数
    def root(self, x):
        visited_nodes = []
        while True:
            p = self.parent[x]
            if p == x:
                # 縮約
                for node in visited_nodes:
                    self.parent[node] = x
                return x
            else:
                visited_nodes.append(x)
                x = p

    # 木の結合を行う。親の配下に入る
    def unite(self, x, y):
        if not self.root(x) == self.root(y):
            if self.rank[x] > self.rank[y]:
                self.parent[self.root(y)] = self.root(x)
            else:
                self.parent[self.root(x)] = self.root(y)
                if self.rank[x] == self.rank[y]:
                    self.rank[self.root(y)] += 1

    def ifSame(self, x, y):
        return self.root(x) == self.root(y)

    # 木の根に到達すまでにたどるノードの配列を返す
    def printDebugInfo(self):
        print([self.root(i) for i in range(self.N)])


N, M = map(int, input().split())
tree = UnionFind(N)
for i in range(M):
    A, B = map(int, input().split())
    tree.unite(A-1, B-1)


bag = {}
for i in range(N):
    boss = tree.root(i)
    if not boss in bag.keys():
        bag[boss] = 1
    else:
        bag[boss] += 1

print(max(bag.values()))
