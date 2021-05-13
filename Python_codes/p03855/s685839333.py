class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        self.rnk = [0] * (n + 1)
        
    def Find_root(self, x):
        if (self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_root(self.root[x])
            return self.root[x]
    
    def Unite(self, x, y):
        x = self.Find_root(x)
        y = self.Find_root(y)
        if (x == y):
            return
        elif (self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if (self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    
    def isSameGroup(self, x, y):
        return self.Find_root(x) == self.Find_root(y)
    
    def Count(self, x):
        return - self.root[self.Find_root(x)]

import collections    
    
n, k, l = map(int, input().split())
union = UnionFind(n)
union1 = UnionFind(n)

for _ in range(k):
    p, q = map(int, input().split())
    union.Unite(p, q)
for _ in range(l):
    p, q = map(int, input().split())
    union1.Unite(p, q)

parents = [(union.Find_root(i), union1.Find_root(i)) for i in range(1, n + 1)]
lc = collections.Counter(parents)
ans = []
for i in range(n):
    ans.append(lc[parents[i]])
print(*ans)