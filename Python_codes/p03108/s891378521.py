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

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
        
n, m = map(int,input().split())
A=[list(map(int,input().split())) for i in range(m)]
uf = UnionFind(n)
ans = [n*(n-1)//2]*m
for i in range(m-1,0,-1):
    a,b=A[i]
    a-=1
    b-=1
    ans[i-1]=ans[i]-(0 if uf.same(a,b) else uf.size(a)*uf.size(b))
    uf.union(a,b)
for r in ans:
    print(r)