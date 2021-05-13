class UnionFind:
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1

    def Count(self, x):
        return -self.root[self.Find_Root(x)]


N,M = map(int,input().split())
UF = UnionFind(N)

for i in range(M):
    A,B = map(int,input().split())
    A -= 1; B -= 1
    UF.Unite(A,B)
ans = 0
for i in range(N):
    ans = max(ans,UF.Count(i))

print(ans)