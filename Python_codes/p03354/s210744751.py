n,m=map(int,input().split())
p=list(map(int,input().split()))


class Uf:
    def __init__(self, N):
        self.p = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def root(self, x): #連結している木の頂点
        if self.p[x] != x:
            self.p[x] = self.root(self.p[x])

        return self.p[x]

    def same(self, x, y): #根が同じか判定する
        return self.root(x) == self.root(y)

    def unite(self, x, y): #くっつける
        u = self.root(x)
        v = self.root(y)

        if u == v: return

        if self.rank[u] < self.rank[v]:
            self.p[u] = v
            self.size[v] += self.size[u]
            self.size[u] = 0
        else:
            self.p[v] = u
            self.size[u] += self.size[v]
            self.size[v] = 0

            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1

    def count(self, x): #連結成分数
        return self.size[self.root(x)]

uf=Uf(n)
for i in range(m):
    x,y=map(int,input().split())
    uf.unite(x-1,y-1)

ans=0
for i in range(n):
    if uf.same(i,p[i]-1):
        ans+=1

print(ans)
