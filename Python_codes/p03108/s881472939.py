# union by sixe
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

N, M = map(int, input().split())
ds = DisjointSet(N+1) 
stack = []
ans = [N*(N-1)//2]
for m in range(M):
    a, b = map(int, input().split())
    stack += [(a, b)]
for m in range(M):
    a, b = stack.pop()
    if ds.same(a, b):
        ans += [ans[-1]]
    else:
        ans += [ans[-1] - ds.size[ds.findSet(a)] * ds.size[ds.findSet(b)]]
        ds.unite(a, b)
ans = ans[::-1]
for i in range(1, M+1):
    print(ans[i])
