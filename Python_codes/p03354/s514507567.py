import sys
input = sys.stdin.readline

class UnionFind():
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
        if self.root[x] > self.root[y]:
            x, y = y, x
        self.root[x] += self.root[y]
        self.root[y] = x 
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)
    def Count(self, x): # xが属するグループのサイズを返す
        return -self.root[self.Find_Root(x)]
    def Members(self, x): # xが属するグループに属する要素をリストで返す
        return [i for i in range(self.n) if self.Find_Root(i)==self.Find_Root(x)]
    def Roots(self): # 全ての根の要素をリストで返す
        return [i for i, x in enumerate(self.root) if x < 0]
    def Group_Count(self): # グループの数を返す
        return len(self.Roots())
    
N, M = map(int, input().split())
uf = UnionFind(N+1)
p = list(map(int, input().split()))
roots = {i:i for i in range(N)}
proots = {i:i for i in range(N)}
for _ in range(M):
    x, y = map(lambda x:int(x)-1, input().split())
    uf.Unite(x, y)

for i in range(N):
    r = uf.Find_Root(i)
    roots[i] = r
    proots[p[i]-1] = r 

ans = 0
for i in range(N):
    if roots[i] == proots[i]:
        ans += 1
print(ans)
