class UnionFind():
    def __init__(self, n):
        self.parents = [-1]*n
        self.rank = [0]*n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            return self.find(self.parents[x])

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

N,M=list(map(int,input().split()))
S=set()
for _ in range(M):
    a,b=list(map(int,input().split()))
    a-=1
    b-=1
    S.add((a,b))

ct=0
for i in S:
    T=S-{i}
    uf=UnionFind(N)
    for (j,k) in T:
        uf.union(j,k)
    a=uf.find(0)
    for l in range(1,N):
        if a!=uf.find(l):
            ct+=1
            break
print(ct)