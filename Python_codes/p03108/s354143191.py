from sys import setrecursionlimit
#setrecursionlimit(10**5)
class UnionFind:
    def __init__(self, n):
        # 親要素のノード番号を格納
        # par[x]=xの時そのノードは根　
        self.par = [i for i in range(n + 1)]
        # rank
        self.rank = [0] * (n + 1)
        self.size = [1] * (n + 1)

    def find(self, x):
        # 根の番号を返す(所属する集合を確認する)
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]

    def check(self, x, y):
        # x,yが同じ集合に属するかどうか調べる
        return self.find(x) == self.find(y)


    def union(self, x, y):
        # 根を探す
        x = self.find(x)
        y = self.find(y)
        if x == y:return
        # rankの小さいものを大きいほうにくっつける
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.size[y] += self.size[x]
        else:
            self.par[y] = x
            self.size[x] += self.size[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def count_group(self, n):
        return len({self.find(x) for x in range(1, n + 1)})

def com_2(n):
    if n == 1:return 0
    return n * (n - 1) // 2

n, m = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(m)]
ab = ab[::-1]
uf = UnionFind(n)

rec = [n * (n - 1) // 2] * m
for i in range(m - 1):
    a, b = ab[i]
    if uf.check(a, b):
        rec[i + 1] = rec[i]
        continue
    a_size = uf.size[uf.find(a)]
    b_size = uf.size[uf.find(b)]
    temp = com_2(a_size) + com_2(b_size) - com_2(a_size + b_size)
    rec[i + 1] = rec[i] + temp
    uf.union(a, b)

rec = rec[::-1]
print(*rec, sep='\n')