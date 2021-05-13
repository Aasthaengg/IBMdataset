class WeightedUnionFind():
    def __init__(self,n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.weight = [0 for _ in range(n)]
    def find(self,x):
        root = x
        stack = [root]
        while self.parents[root] != root:
            root = self.parents[root]
            stack.append(root)
        while stack:
            s = stack.pop()
            self.weight[s] += self.weight[self.parents[s]]
        while self.parents[x] != root:
            parent = self.parents[x]
            self.parents[x] = root
            x = parent
        return root
    def unite(self,x,y,w):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        xrank = self.rank[xroot]
        yrank = self.rank[yroot]
        if xrank < yrank:
            self.parents[xroot] = yroot
            self.weight[xroot] = w-self.weight[x]+self.weight[y]
        else:
            self.parents[yroot] = xroot
            self.weight[yroot] = -w+self.weight[x]-self.weight[y]
            if xrank == yrank:
                self.rank[xroot] += 1
    def diff(self,x,y):
        return self.weight[x]-self.weight[y]

N,M = map(int,input().split())
uf = WeightedUnionFind(N)

for _ in range(M):
    l,r,d = map(int,input().split())
    if uf.find(l-1) == uf.find(r-1):
        if uf.diff(l-1,r-1) != d:
            print('No')
            break
    else:
        uf.unite(l-1,r-1,d)
else:
    print('Yes')