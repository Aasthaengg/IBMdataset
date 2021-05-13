from collections import defaultdict
class UnionFind():
    def __init__(self, n):
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

h, w = map(int, input().split())
S = []
for i in range(h):
    s = input()
    S.append(s)

uf = UnionFind(h*w)

for i in range(h):
    for j in range(w):
        if i < h - 1 and S[i][j] != S[i+1][j]:
            uf.union(i*w+j, (i+1)*w+j)
        if j < w - 1 and S[i][j] != S[i][j+1]:
            uf.union(i*w+j, i*w+j+1)

ans = 0

d = defaultdict(int)

for i in range(h*w):
    if S[i//w][i%w] == '.':
        d[uf.find(i)] += 1

for i, x in enumerate(uf.parents):
    if x < 0:
        # print(-x, d[i])
        cnt = -x
        ans += d[uf.find(i)] * (cnt-d[i])

print(ans)


            
