import sys
input = sys.stdin.readline
 
class Unionfind:
    def __init__(self, n):
        self.par = [-1]*n
        self.rank = [1]*n
    
    def root(self, x):
        p = x
        
        while not self.par[p]<0:
            p = self.par[p]
        
        while x!=p:
            tmp = x
            x = self.par[x]
            self.par[tmp] = p
        
        return p
    
    def unite(self, x, y):
        rx, ry = self.root(x), self.root(y)
        
        if rx==ry: return False
        
        if self.rank[rx]<self.rank[ry]:
            rx, ry = ry, rx
        
        self.par[rx] += self.par[ry]
        self.par[ry] = rx
    
        if self.rank[rx]==self.rank[ry]:
            self.rank[rx] += 1
    
    def is_same(self, x, y):
        return self.root(x)==self.root(y)
    
    def count(self, x):
        return -self.par[self.root(x)]

N, M = map(int, input().split())
p = list(map(lambda x: x-1, map(int, input().split())))
uf = Unionfind(N)

for _ in range(M):
    x, y = map(int, input().split())
    uf.unite(p[x-1], p[y-1])

ans = 0

for i in range(N):
    if uf.is_same(p[i], i):
        ans += 1

print(ans)