# D - Equals

class UnionFind():
    def __init__(self, n):
        self.par = [-1]*n
    
    def _find(self, x):
        if self.par[x] < 0:
            return x
        self.par[x] = self._find(self.par[x])
        return self.par[x]

    def _union(self, x, y):
        x = self._find(x)
        y = self._find(y)
        if (x==y): 
            return False
        if (self.par[x]>self.par[y]):
            x, y = y, x
        self.par[x] += self.par[y]
        self.par[y] = x
        return True
    
    def _is_same_group(self, x, y):
        return self._find(x)==self._find(y)
    

N, M = map(int, input().split())
P = [int(p) for p in input().split()]
u = UnionFind(N+1)
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    u._union(P[x], P[y])

ans = 0
for i in range(N):
    if u._is_same_group(P[i], P[P[i]-1]):
        ans += 1

print(ans)