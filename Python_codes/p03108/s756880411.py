import sys
def input():
    return sys.stdin.readline()[:-1]
n,m = map(int,input().split())
ab = []
for i in range(m):
     ab.append(list(map(int,input().split())))
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)
    def Find_Root(self,x):
        if self.root[x]<0:return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)
    def Count(self, x):
        return -self.root[self.Find_Root(x)]
land = UnionFind(n)
all = int(n*(n-1)/2)
lis = [all]
for i in range(m-1):
    [a,b] = ab[-1-i]
    if land.Find_Root(a) != land.Find_Root(b):
        all -= land.Count(a)*land.Count(b)
    land.Unite(a,b)
    lis.append(all)
#print(lis)
for i in range(m):
    print(lis[-1-i])
