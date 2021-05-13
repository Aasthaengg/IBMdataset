class UnionFind():
    def __init__(self, n):
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


N,M=map(int,input().split())
A=[0]*M
B=[0]*M
for i in range(M):
    A[i],B[i]=map(int,input().split())

uf=UnionFind(N+1)
for i in range(M):
    uf.union(A[i],B[i])
a=[0]*(N+1)
con=0

for i in uf.parents:
    if(i<0):
        con=con+1

print(con-2)
