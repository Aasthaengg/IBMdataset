class UnionFind:
    MAX_N = 0
    PAR  = [] 
    RANK = []

    def __init__(self,n):
        self.MAX_N = n
        self.PAR = [ i for i in range(n)]
        self.RANK= [ 0 ] * n

    def find(self,x):
        if self.PAR[x] == x:
            return x
        else:
            self.PAR[x] = self.find(self.PAR[x])
            return self.PAR[x] 

    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.RANK[x] < self.RANK[y]:
            self.PAR[x] = y
        else:
            self.PAR[y] = x
            if self.RANK[x] == self.RANK[y]:
                self.RANK[x] += 1

    def same(self,x,y):
        return self.find(x) == self.find(y)

N,K,L = map(int,input().split())
path = UnionFind(N+1)
for _ in range(K):
    p,q = map(int,input().split())
    path.union(p,q)
rail = UnionFind(N+1)
for _ in range(L):
    p,q = map(int,input().split())
    rail.union(p,q)

Data = {}
for i in range(1,N+1):
    p = path.find(i)
    r = rail.find(i)
    k = str(p)+"-"+str(r)
    if k in Data.keys():
        Data[k] += 1
    else:
        Data[k] = 1

for i in range(1,N+1):
    p = path.find(i)
    r = rail.find(i)
    k = str(p)+"-"+str(r)
    print( Data[k], end= ' ')
