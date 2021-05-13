class UnionFind():
    def __init__(self, n):
        self.parents = list(range(n))
        self.rank = [0] * n

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

        if self.rank[x] < self.rank[y]:
            self.parents[x] = y
        else:
            self.parents[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

n,m = map(int,input().split())
A = [0]*m
B = [0]*m
for i in range(m):
    A[i],B[i] = map(int,input().split())

ans = 0
for i in range(m):
    u = UnionFind(n)
    for j in range(m):
        if i==j:continue
        a,b = A[j]-1,B[j]-1
        u.union(a,b)
    for j in range(n):
        u.find(j)
    if len(set(u.parents))!=1:
        ans+=1
print(ans)



