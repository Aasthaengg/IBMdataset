class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        """ 根を見つける関数を定義（同時にxを直接根にくっつける操作も行う）"""
        tmp = []
        parents = self.parents
        while parents[x] >= 0:
            tmp.append(x)
            x = parents[x]
        for y in tmp:
            parents[y] = x
        return x

    def union(self, x, y):
        """ 二つの木をくっつける（子を多く持つ方を根とした親子関係）。これは破壊的操作を行う。"""
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        """ xとyが同じ根の子かを判定 """
        return self.find(x) == self.find(y)

    def size(self, x):
        """ xの根のparent（= 要素数）を返す """
        return -self.parents[self.find(x)]

    def members(self, x):
        """ xが属するグループの要素をリストとして返す """
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        """ 全ての根の要素をリストとして返す """
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        """ グループの数を返す """
        return len(self.roots())

    def size_list(self):
        """ 各グループの要素数のリストを返す(根の番号は返さない) """
        return [-x for x in self.parents if x < 0]

    def all_group_members(self):
        """ {根:[根の子のリスト],...}を辞書で返す """
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


##############################################################################################################
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = list(map(int, input().split()))
U = UnionFind(N)
for _ in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    U.union(a, b)
res = 0
for i, p in enumerate(P):
    if U.same(p-1,i):
        res += 1
print(res)
