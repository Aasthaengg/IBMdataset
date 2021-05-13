class Unionfind:

    __slots__ = ['nodes','rank']

    def __init__(self, n):
        self.nodes = list(range(n))
        self.rank = [0]*n

    def root(self, x):
        if self.nodes[x] == x:
            return x
        else:
            root_x = self.root(self.nodes[x])
            self.nodes[x] = root_x
            return root_x

    def unite(self, x, y):
        x = self.root(x); y = self.root(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.rank[x] += self.rank[y]
        self.nodes[y] = x

    def same(self, x, y):
        return self.root(x) == self.root(y)

around = [(0,1),(1,0),(0,-1),(-1,0)]

H,W = map(int,input().split())
grid = [list(input()) for _ in range(H)]
uf = Unionfind(H*W)

for i in range(H):
    for j in range(W):
        for di,dj in around:
            ni = i + di; nj = j + dj
            if not(0 <= ni <= H-1 and 0 <= nj <= W-1):
                continue
            x = W*i+j; y = W*ni+nj
            if grid[i][j] != grid[ni][nj]:
                uf.unite(x,y)

for v in range(H*W):
    uf.root(v)

group = [[0]*2 for _ in range(H*W)]

for i,line in enumerate(grid):
    for j,c in enumerate(line):
        parent = uf.nodes[W*i+j]
        if c == ".":
            group[parent][0] += 1
        if c == "#":
            group[parent][1] += 1

ans = sum([w*b for w,b in group])
print(ans)