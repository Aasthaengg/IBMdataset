# 86
# ABC 075 C - Bridge

class UnionFindTree():
    def __init__(self, n):
        self.rank = [0] * n
        self.par = [x for x in range(n)]
        
    def find(self, x):
        if x == self.par[x]:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
        elif self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            self.rank[x] += 1
    
    def same(self, x, y):
        return (self.find(x) == self.find(y))

n, m = map(int, input().split())
ab_l = [[int(x)-1 for x in input().split()] for y in range(m)]

ans = 0

for i in range(m):
    UF = UnionFindTree(n)
    for j in range(m):
        if i != j:
            UF.unite(ab_l[j][0], ab_l[j][1])
    for j in range(1,n):
        if not UF.same(0, j):
            ans += 1
            break

print(ans)