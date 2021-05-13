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

N,M = map(int,input().split())
Data = list(map(int,input().split()))
graph = UnionFind(N+1)
for _ in range(M):
    x1,y1 = map(int,input().split())
    graph.union(x1,y1)

ans = 0
for i in range(1,N+1):
    if graph.same(i,Data[i-1]):
        ans+=1

print(ans)
