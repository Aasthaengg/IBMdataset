class UnionFind():
    def __init__(self, n):
        self.n = n
        self.par = [-1]*n 
    def find(self, x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def roots(self):
        return [i for i, x in enumerate(self.par) if x<0]
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)      
        if x==y:
            return        
        if self.par[x] > self.par[y]:
            x, y = y, x       
        self.par[x] += self.par[y]
        self.par[y] = x
    def group_count(self):
        return len(self.roots())

N, M = map(int, input().split())
UF = UnionFind(N)
for _ in range(M):
  a, b = map(int, input().split())
  UF.union(a-1, b-1)
print(UF.group_count()-1)