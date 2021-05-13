class UnionFind:
    def __init__(self, n):
        self.r = [-1 for i in range(n)]
    
    def root(self, x):
        if self.r[x] < 0:
            return x
        self.r[x] = self.root(self.r[x])
        return self.r[x]
    
    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.r[x] < self.r[y]:
            temp = x
            x = y
            y = temp
        self.r[x] += self.r[y]
        self.r[y] = x
        return True
    
    def size(self, x):
        return -self.r[self.root(x)]

n, m = map(int, input().split())
UF = UnionFind(n)
for i in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    UF.unite(a, b)

ans = 0
for i in UF.r:
    if i < 0:
        ans += 1

print(ans-1)