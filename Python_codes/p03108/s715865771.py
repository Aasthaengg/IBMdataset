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
        if x == y:return -1
        # rankの小さいものを大きいほうにくっつける
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            temp = self.size[x]
            self.size[y] += temp
            temp1 = self.size[y]
        else:
            self.par[y] = x
            temp = self.size[y]
            self.size[x] += temp
            temp1 = self.size[x]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
        return (temp, temp1)

    def count_group(self):
        return len({self.find(x) for x in range(1, n + 1)})

n, m = map(int,input().split())
ab = [list(map(int,input().split())) for i in range(m)]

uf = UnionFind(n)
inc = [n * (n - 1) // 2] * m
for i in range(m - 1):
    a, b = ab[- i - 1]
    rec = uf.union(a, b)
    if rec == -1:
        inc[-i-2] = inc[-i-1]
        continue

    temp = rec[1] - rec[0]
    inc[-i-2] = max(inc[-i-1] - temp * rec[0], 0)

    #print(uf.size,inc,rec,temp)
print(*inc, sep = '\n')
