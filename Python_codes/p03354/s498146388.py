n,m=map(int,input().split())
p=list(map(int,input().split()))

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
#uf = UnionFind(n) #初期化
#uf.union(0, 2)#グループを併合
#uf.find(0) #親要素が変える

uf=UnionFind(n)
for _ in range(m):
    x,y=map(int,input().split())
    uf.union(x-1,y-1)
cnt=0
for i in range(n):
    
    if uf.find(i)==uf.find(p[i]-1):
        cnt+=1

print(cnt)