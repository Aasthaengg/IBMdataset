#!/usr/bin/env python

n, m = map(int, input().split())
a = [0 for _ in range(m)]
b = [0 for _ in range(m)]
for i in range(m):
    a[i], b[i] = map(int, input().split())
    a[i] -= 1
    b[i] -= 1

class UnionFind():
    def __init__(self, n): 
        self.n = n 
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.sizes = [1 for _ in range(n)]

    def root(self, x): 
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x]) # 圧縮経路
            return self.par[x]
            # return root(par[x]) # 圧縮しない場合

    def same(self, x, y): 
        return self.root(x) == self.root(y)

    def unite(self, x, y): 
        rx = self.root(x)
        ry = self.root(y)
        if rx == ry: 
            return

        # par[rx] = ry # naiveな連結

        # 低い木を高い方にくっつける。
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.sizes[ry] += self.sizes[rx]
        else:
            self.par[ry] = rx
            self.sizes[rx] += self.sizes[ry]

        # rx木とry木の高さが同じならば、rx木を深くする。
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1

    def size(self, x): 
        '''
        xが属するグループのサイズを返す
        (連結成分の大きさ)
        '''
        return self.sizes[self.root(x)]

    def roots(self):
        '''
        全ての頂点の根のlistを返す   
        '''
        return [self.root(i) for i in range(self.n)]

    def connected(self):
        ''' 
        連結成分の数を返す
        '''
        #return len(set(self.par))
        return len(set(self.roots()))

uf = UnionFind(n)
for i in range(m):
    uf.unite(a[i], b[i])

ans = uf.connected()-1
print(ans)
