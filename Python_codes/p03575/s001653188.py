class DisjointSet:
    def __init__(self, size):
        self.size = [0 for i in range(size)]
        self.p = [0 for i in range(size)]
        for i in range(size):
            self.makeSet(i)
    
    def makeSet(self, x):
        self.p[x] = x
        self.size[x] = 1

    def same(self, x, y):
        return self.findSet(x) == self.findSet(y)

    def unite(self, x, y):
        self.link(self.findSet(x), self.findSet(y))

    def link(self, x, y):
        if self.size[x] > self.size[y]:
            self.p[y] = x
            self.size[x] += self.size[y]
        else:
            self.p[x] = y
            self.size[y] += self.size[x]
    
    def findSet(self, x):
        if x != self.p[x]:
            self.p[x] = self.findSet(self.p[x])
        return self.p[x]

    def getSize(self, x):
        return self.size[ds.findSet(x)]

N, M = map(int, input().split())
A = []
B = []
for i in range(M):
    a, b = map(int, input().split())
    A += [a]
    B += [b]
ans = 0
for i in range(M):
    ds = DisjointSet(N+1)
    for j, (a, b) in enumerate(zip(A, B)):
        if i == j:
            continue
        ds.unite(a, b)
    if len(set([ds.findSet(j) for j in range(1, N+1)])) != 1:
        ans += 1
print(ans)