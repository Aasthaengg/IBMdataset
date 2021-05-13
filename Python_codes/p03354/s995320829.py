N,M = map(int,input().split())
p = [0] + [int(x) for x in input().split()]

class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.par[x] == x:    return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:    self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

UF = UnionFind(N)
for _ in range(M):
    x,y = map(int,input().split())
    UF.union(x, y)

unionUF, unionp = [set() for _ in range(N+1)], [set() for _ in range(N+1)]
for i in range(1, N+1):
    temp = UF.find(i)
    unionUF[temp].add(i)
    unionp[temp].add(p[i])

ans = 0
for i in range(len(unionUF)):
    ans += len(unionUF[i] & unionp[i])
print(ans)