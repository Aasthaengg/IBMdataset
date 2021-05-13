class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)
        
    def find_root(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find_root(self.root[x])
            return self.root[x]
        
    def unite(self, x, y):
        x = self.find_root(x)
        y = self.find_root(y)
        if x == y:
            return
        elif self.rnk[x] > self.rnk[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if self.rnk[x] == self.rnk[y]:
                self.rnk[y] += 1
                
    def isSameGroup(self, x, y):
        return self.find_root(x) == self.find_root(y)
    
    def count(self, x):
        return -self.root[self.find_root(x)]
    
    
    
N,M = map(int, input().split())
P = [int(p) for p in input().split()]
L = []
for i in range(M):
    L.append([int(x) for x in input().split()])
    
tree = UnionFind(N)
for i in range(M):
    tree.unite(P[L[i][0]-1], P[L[i][1]-1])
    
ans = 0
for i in range(N):
    if tree.isSameGroup(P[i], i+1):
        ans += 1
        
print(ans)