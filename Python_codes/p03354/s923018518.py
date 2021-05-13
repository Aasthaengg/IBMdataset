class UnionFind:
    def __init__(self, data):
        self.parent = {}
        self.rank = {}
        for i in range(1, data+1):
            self.parent[i] = i
            self.rank[i] = 0
 
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
 
    def same(self, x, y):
        return self.find(x) == self.find(y)
 
 
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.find(x) == self.find(y):
            return
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            return
        else:
            self.parent[x] = y
            if self.rank[x] == self.rank[y]: self.rank[y] += 1
            return

N, M = map(int, input().split())
P = list(map(int, input().split()))
L = []
for i in range(M):
    L.append([int(x) for x in input().split()])
tree = UnionFind(N)
for i in range(M):
    tree.unite(P[L[i][0]-1], P[L[i][1]-1])
ans = 0
for i in range(N):
    if tree.same(P[i], i+1):
        ans += 1
print(ans)