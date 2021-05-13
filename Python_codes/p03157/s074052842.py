import sys
def input():
    return sys.stdin.readline()[:-1]
inf=float("inf")
h,w=map(int,input().split())
s=[input() for i in range(h)]
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
uf = WeightedUnionFind(h*w)
for i in range(h):
    for j in range(w):
        if (i+1)+1<=h and s[i][j]!=s[i+1][j]:
            uf.union(i*w+j+1,(i+1)*w+j+1,0)
        if (j+1)+1<=w and s[i][j]!=s[i][j+1]:
            uf.union(i*w+j+1,i*w+j+2,0)
        if (i+1)-1>=1 and s[i][j]!=s[i-1][j]:
            uf.union(i*w+j+1,(i-1)*w+j+1,0)
        if (j+1)-1>=1 and s[i][j]!=s[i][j-1]:
            uf.union(i*w+j+1,i*w+j,0)
li=[[0,0] for i in range(h*w+1)]
for i in range(h):
    for j in range(w):
        if s[i][j]=="#":
            li[uf.find(i*w+j+1)][0]+=1
        else:
            li[uf.find(i*w+j+1)][1]+=1
# print(li)
ans=0
for i in range(h):
    for j in range(w):
        ans+=li[i*w+j+1][0]*li[i*w+j+1][1]
print(ans)