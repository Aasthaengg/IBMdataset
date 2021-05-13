import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.data = [0] * N
        for i in range(N):
            self.data[i] = i
            
    def get_root(self, x):
        r = self.data[x]
        if r == x:
            return r
        p = self.get_root(r)
        self.data[x] = p
        
        return p
    
    def unite(self, x, y):
        rx = self.get_root(x)
        ry = self.get_root(y)
        
        if rx != ry:
            self.data[rx] = ry

    def same(self, x, y):
        return self.get_root(x) == self.get_root(y)

N, K, L = map(int, input().split())
LA = [[int(v) - 1 for v in input().split()] for _ in range(K)]
LB = [[int(v) - 1 for v in input().split()] for _ in range(L)]

u1 = UnionFind(N)
for x, y in LA:
    u1.unite(x, y)
    
u2 = UnionFind(N)
for x, y in LB:
    u2.unite(x, y)

result = {}
for i in range(N):
    a = u1.get_root(i)
    b = u2.get_root(i)
    
    if result.get((a, b)) == None:
        result[(a, b)] = 0
    result[(a, b)] += 1
    
for i in range(N):
    a = u1.get_root(i)
    b = u2.get_root(i)
    
    print(result[(a, b)], end = "")
    if i != N - 1:
        print(" ", end = "")
    else:
        print()
