N, M = map(int, input().split())
p = list(map(int, input().split()))

num = [0 for _ in range(N+1)]

class Unionfind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * (n+1)
        
    def find(self, x):
        if(self.parents[x] < 0):
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
        
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if(x == y):
            return
        
        if(self.parents[x] > self.parents[y]):
            x, y = y, x
            
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):
        return -self.parents[self.find(x)]
    
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}
    
    def __str__(self):
        return '\n'.join('{}:{}'.format(r, self.members(r)) for r in self.roots())
    
    
uf = Unionfind(N+1)
        
for _ in range(M):
    x, y = map(int, input().split())
    uf.union(x, y)
ans = 0
for i in range(N):
    if(uf.find(i+1) == uf.find(p[i])):
        ans += 1
print(ans)