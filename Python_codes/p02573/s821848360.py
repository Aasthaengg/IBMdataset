class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.sum = [1] * (n+1)

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
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
            self.sum[y] += self.sum[x]
        else:
            self.par[y] = x
            self.sum[x] += self.sum[y]
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int,input().split())
A = [0] * M
B = [0] * M

uni = UnionFind(N)

for i in range(M):
    A[i], B[i] = map(int,input().split())
    uni.union(A[i],B[i])


print(max(uni.sum))
















"""
N, M = map(int, input().split())

par = list(range(N))
rank = [1] * N
size = [1] * N


def find(x):
    if par[x] == x:
        return x
    else:
        return find(par[x])


def unite(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if rank[x] < rank[y]:
        x, y = y, x
    par[y] = x
    size[x] += size[y]
    if rank[x] == rank[y]:
        rank[x] += 1


for i in range(M):
    a, b = [int(i) - 1 for i in input().split()]
    unite(a, b)

print(max(size))"""

