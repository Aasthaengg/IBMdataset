class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """
        要素xが属するグループの根を返す
        """
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        """
        要素xが属するグループと要素yが属するグループを併合
        """
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        """
        要素xが属するグループのサイズを返す
        """
        return -self.parents[self.find(x)]

    def same(self, x, y):
        """
        要素x, yが同じグループかどうか
        """
        return self.find(x) == self.find(y)

    def members(self, x):
        """
        要素xが属するグループの要素をリストで返す
        """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """
        すべての根の要素をリストで返す
        """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """
        グループの数を返す
        """
        return len(self.roots())

    def all_group_members(self):
        """
        {ルート要素: [そのグループの要素, ...], ...}を返す
        """
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        """
        print()での表示用
        """
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())
    
N, M = map(int, input().split())
uf = UnionFind(N)
P = list(map(int, input().split()))
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    uf.union(P[a] - 1, P[b] - 1)

res = 0
for i, p in enumerate(P):
    if uf.same(p - 1, i):
        res += 1

print(res)
