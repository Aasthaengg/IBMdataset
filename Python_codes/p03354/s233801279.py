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

n, m = map(int, input().split())
p = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(m)]
uf = UnionFind(n+1)
for x, y in xy:
    uf.Unite(p[x-1], p[y-1])
ans = 0
for i in range(n):
    if uf.isSameGroup(i+1, p[i]):
        ans += 1
print(ans)