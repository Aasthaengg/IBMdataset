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

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]


H, W = map(int, input().split(" "))
S = []
for _ in range(H):
    S.append(input())

# calc connected componets
con_comp = UnionFind(H * W)
for i in range(H):
    for j in range(W):
        for (dh, dw) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if i + dh < 0 or j + dw < 0 or i + dh >= H or j + dw >= W:
                continue
            if S[i][j] != S[i + dh][j + dw]:
                con_comp.union(i * W + j, (i + dh) * W + j + dw)

# enum white
white = {}
for i in range(H):
    for j in range(W):
        if S[i][j] == '.':
            if con_comp.find(i * W + j) in white:
                white[con_comp.find(i * W + j)] += 1
            else:
                white[con_comp.find(i * W + j)] = 1

# count black
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#' and con_comp.size(i * W + j) > 1:
            ans += white[con_comp.find(i * W + j)]

print(ans)