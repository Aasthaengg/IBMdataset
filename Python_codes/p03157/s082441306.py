H,W = map(int,input().split())
S = [input() for i in range(H)]

class UnionFind:
    def __init__(self,N):
        self.parent = [i for i in range(N)]
        self._size = [1] * N
        self.count = 0
    def root(self,a):
        if self.parent[a] == a:
            return a
        else:
            self.parent[a] = self.root(self.parent[a])
            return self.parent[a]
    def is_same(self,a,b):
        return self.root(a) == self.root(b)
    def unite(self,a,b):
        ra = self.root(a)
        rb = self.root(b)
        if ra == rb: return
        if self._size[ra] < self._size[rb]: ra,rb = rb,ra
        self._size[ra] += self._size[rb]
        self.parent[rb] = ra
        self.count += 1
    def size(self,a):
        return self._size[self.root(a)]

uf = UnionFind(H*W)
for i in range(H):
    for j in range(W):
        if i < H-1 and S[i][j] != S[i+1][j]:
            uf.unite(i*W+j, (i+1)*W+j)
        if j < W-1 and S[i][j] != S[i][j+1]:
            uf.unite(i*W+j, i*W+j+1)
for i in range(H*W):
    uf.root(i)

from collections import defaultdict
bl = defaultdict(lambda: 0)
wh = defaultdict(lambda: 0)
for i in range(H):
    for j in range(W):
        v = i*W+j
        r = uf.root(v)
        if S[i][j]=='#':
            bl[r] += 1
        else:
            wh[r] += 1

ans = 0
for k in bl.keys():
    ans += bl[k] * wh[k]
print(ans)