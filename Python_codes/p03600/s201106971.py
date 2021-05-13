class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def size(self, x):
        if self.parents[x] < 0:
            return -self.parents[x]
        else:
            self.parents[x] = self.size(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

n = int(input())
A = [list(map(int,input().split())) for i in range(n)]
M = [[j for j in i] for i in A]

for k in range(n):
    for i in range(n):
        for j in range(n):
            M[i][j] = min(M[i][j], M[i][k] + M[k][j])

b = 0
if A != M:
    print(-1)
else:
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            b = 0
            for k in range(n):
                if k != i and k != j and M[i][j] == M[i][k] + M[k][j]:
                    b = 1
                    break
            if b == 0:
                ans += A[i][j]
    print(ans)