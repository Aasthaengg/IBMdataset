class UnionFind():
    def __init__(self, N):
        self.N = N
        self.par = [n for n in range(N)]
        self.rank = [1] * N
        
    def find(self, u):
        if self.par[u] == u:
            return u
        else:
            return self.find(self.par[u])
    
    def union(self, u, v):

        pu = self.find(u)
        pv = self.find(v)

        if pu == pv: 
            return

        if self.rank[pu] < self.rank[pv]:
            self.par[pu] = pv
            self.rank[pv] += self.rank[pu]

        else: # self.rank[pu] > self.rank[pv]
            self.par[pv] = pu
            self.rank[pu] += self.rank[pv]
 
N, M = map(int, input().split())
UF = UnionFind(N)
for _ in range(M):
    A, B = map(int, input().split())
    A, B = A-1, B-1
    UF.union(A, B)


ret = 0

for n in range(N):
    ret = max(ret, UF.rank[n])

print(ret)
