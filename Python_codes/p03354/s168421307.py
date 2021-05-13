import collections

N,M = map(int,(input().split()))
p = list(map(int,(input().split())))
line = [[] for _ in range(N+1)]
for i in range(M):
    a,b = map(int,(input().split()))
    line[a-1].append(b-1)

class UnionFind:

    def __init__(self, n):
        self.par =  [-1] * n
        self.rank = [0] * n
    
    def root(self,x):
        if self.par[x] < 0:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]

    def union(self, x, y):
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return
        else:
            if self.rank[x] <self.rank[y]:
                self.par[y] += self.par[x] # 負+負でsize管理 
                self.par[x] = y
            else:
                self.par[x] += self.par[y]
                self.par[y] = x
                if self.rank[x] == self.rank[y]: # 負+負でsize管理 
                    self.rank[x] += 1
    
    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.par[self.root(x)]

Tree = UnionFind(N)
for i in range(N):
    for node in line[i]:
        Tree.union(i,node)

d = [[] for _ in range(N)]
e = [[] for _ in range(N)]
for i in range(N):
    d[Tree.root(i)].append(i)
    d[Tree.root(i)].append(p[i]-1)

ans = 0
for i in range(N):
    ans += len(d[i]) - len(set(d[i]))

print(ans)