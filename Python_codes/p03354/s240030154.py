class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

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
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    # 同じ集合に属するか判定
    def same_check(self, x, y):
        return self.find(x) == self.find(y)


N, M = map(int, input().split(' '))
P = [int(c) for c in input().split(' ')]

uft = UnionFind(N)
for _ in range(M):
    x, y = map(int, input().split(' '))
    x -= 1
    y -= 1
    uft.union(x, y)

ans = 0
for i in range(N):
    if i+1 == P[i]:
        ans += 1
    else:
        if uft.find(i) == uft.find(P[i]-1):
            ans += 1

print(ans)