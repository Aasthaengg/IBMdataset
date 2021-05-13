class UnionFind:
    def __init__(self,n):
        self.table = [-1]*n

    def root(self,x):
        stack = []
        tbl = self.table
        while tbl[x]>=0:
            stack.append(x)
            x = tbl[x]
        for y in stack:
            tbl[y] = x
        return x

    def find(self,x,y):
        return self.root(x)==self.root(y)
    def union(self,x,y):
        r1 = self.root(x)
        r2 = self.root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -=1
        else:
            self.table[r1] = r2
N,M = map(int,input().split())
AB = []
for i in range(M):
    AB.append(list(map(int,input().split())))
uf = UnionFind(N)
for i in range(M):
    uf.union(AB[i][0]-1,AB[i][1]-1)
r = [0]*N
for i in range(N):
    r[i]=uf.root(i)
print(len(set(r))-1)