class UnionFind:
    def __init__(self, n):
        '木の初期化をする'
        self.p = [-1] * n
        self.rank = [1]*n
        self.b = [0]*n
        self.w = [0]*n
        self.parent = set(range(n))

    def find(self, x):
        'x の親を返す'
        if self.p[x] == -1:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def unite(self, x, y):
        'rankの低い親を高い方のの親にする'
        if not self.same(x,y):
            x = self.find(x)
            y = self.find(y)
            if self.rank[x] > self.rank[y]:
                x,y = y,x
            elif self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.b[y] += self.b[x]
            self.w[y] += self.w[x]
            self.p[x] = y
            if x in self.parent:
                self.parent.remove(x)
            return True
        else:
            return False

    def same(self, x, y):
        return self.find(x) == self.find(y)

h,w = map(int,input().split())
uf = UnionFind(h*w)
S = []
for i in range(h):
    S.append(input())
    for j,s in enumerate(S[i]):
        if s == '#':
            uf.b[i*w+j] += 1
        else:
            uf.w[i*w+j] += 1

for i in range(h):
    for j in range(w):
        for di,dj in [[1,0],[0,1]]:
            ni = i+di
            nj = j+dj
            if ni < h and nj < w and S[i][j] != S[ni][nj]:
                uf.unite(i*w+j,ni*w+nj)
ans = 0
for p in uf.parent:
    ans += uf.b[p] * uf.w[p]
print(ans)
