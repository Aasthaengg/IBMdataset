class UnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]

    def find(self,x):
        root = x
        while self.parents[root] != root:
            root = self.parents[root]
        while self.parents[x] != root:
            parent = self.parents[x]
            self.parents[x] = root
            x = parent
        return root

    def unite(self,x,y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        xrank = self.rank[xroot]
        yrank = self.rank[yroot]
        if xrank < yrank:
            self.parents[xroot] = yroot
        elif xrank == yrank:
            self.parents[yroot] = xroot
            self.rank[yroot] += 1
        else:
            self.parents[yroot] = xroot

N,M = map(int,input().split())
P = list(map(int,input().split()))

uf = UnionFind(N)

for _ in range(M):
    x,y = map(int,input().split())
    uf.unite(x-1,y-1)

ans = 0

for i in range(N):
    if uf.find(i) == uf.find(P[i]-1):
        ans += 1

print(ans)