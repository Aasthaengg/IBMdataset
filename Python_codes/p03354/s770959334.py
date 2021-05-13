class UnionFind():
    """
    UnionFindTreeのクラス
    
    Attributes:
    n: int: ノード数
    parents: そのノードが属する木の根を格納, 根の場合は-1

    """
    def __init__(self, n):
        """ノード数nで初期化"""
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """ノードxが属するグループの根を返す"""
        if self.parents[x] < 0:
            return x
        else:
            #経路圧縮
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """xが属するグループとyが属するグループを併合"""
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """xが属するグループの要素数を返す"""
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """x, yが同じグループに属するかどうかを返す"""
        return self.find(x) == self.find(y)

    def members(self, x):
        """xが属するグループ内の要素をリストで返す"""
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """全ての根に対する要素をリストで返す"""
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """グループの総数を返す"""
        return len(self.roots())

    def all_group_members(self):
        """{root: [そのグループの要素リスト]}の辞書を返す"""
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        """printデバッグ用. root: [要素リスト]をstrで返す"""
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())



N,M=map(int,input().split())
p= [0] + list(map(int, input().split()))
uf = UnionFind(N+1)
for _ in range(M):
    x,y=map(int, input().split())
    uf.union(x,y)
ans = 0
for i in range(1, 1+N):
    if p[i]==i:
        ans += 1
    else:
        if uf.same(i, p[i]):
            ans += 1
print(ans)