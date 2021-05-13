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
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    def size(self, x):
        return -self.parents[self.find(x)]
    def same(self, x, y):
        return self.find(x) == self.find(y)
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    def group_count(self):
        return len(self.roots())

N = int(input())
B = [list(map(int,input().split())) for _ in range(N)]

ans = 10**10

for i in range(N):
    for j in range(N):

        if i==j:
            continue

        p = B[i][0]-B[j][0]
        q = B[i][1]-B[j][1]
        uf = UnionFind(N)

        for k in range(N):
            for l in range(N):

                if k==l:
                    continue

                if B[k][0]-B[l][0] == p and B[k][1]-B[l][1] == q:
                    uf.union(k,l)

        ans = min(ans,uf.group_count())

print(ans if N != 1 else 1)