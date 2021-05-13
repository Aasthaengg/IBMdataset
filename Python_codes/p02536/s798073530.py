n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(m)]

class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight = [0] * (n+1)
        self.sizes = [1] * (n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def union(self, x, y, w=1):
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.sizes[ry] += self.size(rx)
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.sizes[rx] += self.size(ry)
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]

    def size(self, x):
        return self.sizes[self.find(x)]

uf=WeightedUnionFind(n)

for a,b in ab:
    uf.union(a,b)

s=set()
ans=0
for i in range(n):
    if not uf.find(i+1) in s:
        ans+=1
        s.add(uf.find(i+1))
print(ans-1)