#Satoooh  https://www.planeta.tokyo/entry/6464/
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]  # 親
        self.rank = [1] * n  # 木の高さ
        self.size = [1] * n  # size[i] は i を根とするグループのサイズ

    def find(self, x):  # x の根を返す
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
            return self.parent[x]

    def unite(self, x, y):  # x, y の属する集合を併合する
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def is_same(self, x, y):  # x, y が同じ集合に属するか判定する
        return self.find(x) == self.find(y)

    def group_size(self, x):  # x が属する集合の大きさを返す
        return self.size[self.find(x)]

    def __str__(self):  # print 表示用
        return '\n'.join('{}: {}'.format(r, self.group_members(r)) for r in self.roots())


N, M = map(int, input().split())
bridge = [list(map(int, input().split())) for _ in range(M)]
ans = [0]*M
uf = UnionFind(N)

# うしろからつないでいく
ans[M-1] = N*(N-1)//2
for i in range(M-2, -1, -1):
    A, B = bridge[i+1]
    if uf.is_same(A-1, B-1):
        ans[i] = ans[i+1]
    else:
        ans[i] = ans[i+1] - uf.group_size(A-1) * uf.group_size(B-1)
    uf.unite(A-1, B-1)

for a in ans:
    print(a)