class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
    def find(self, x):
        if self.parents[x] == x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.parents[y] = x
N,M=map(int,input().split())
uf=UnionFind(N)
for i in range(M):
    a,b=map(int,input().split())
    a-=1;b-=1
    uf.union(a,b)
print(len(set([uf.find(i)for i in range(N)]))-1)