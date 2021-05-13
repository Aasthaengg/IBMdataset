import sys
def input():
    return sys.stdin.readline()[:-1]

class WeightedUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight = [0] * (n+1)


    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def union(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]

inf=float("inf")
n,m=map(int,input().split())
p=list(map(int,input().split()))
xy=[list(map(int,input().split())) for i in range(m)]

uf=WeightedUnionFind(n+1)
cnt=0
for i in range(m):
    uf.union(xy[i][0],xy[i][1],0)
for i in range(n):
    if uf.same(i+1,p[i]):
        cnt+=1
print(cnt)