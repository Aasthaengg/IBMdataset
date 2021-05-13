P = 10**9 + 7

class UnionFind():
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0] * n

    def root(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.par[x] = y
            else:
                self.par[y] = x
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def samegrp(self, x, y):
        return self.root(x) == self.root(y)

N, M = [int(x) for x in input().split()]
X = UnionFind(N + 1)
for i in range(M):
    X.union(0, int(input()))

dp = [0]*(N + 1)
dp[0] = 1
if X.samegrp(0, 1):
    dp[1] = 0
else:
    dp[1] = 1
for i in range(2, N + 1):
    if X.samegrp(0, i):
        dp[i] = 0
    else:
        dp[i] = (dp[i - 1] + dp[i - 2]) % P

ans = dp[N]
print(ans)