class WUnionFind:
    MAX_N = 0
    PAR  = [] 
    RANK = []
    DIFF_WEIGHT=[]

    def __init__(self,n):
        self.MAX_N = n
        self.PAR = [ i for i in range(n)]
        self.RANK= [ 0 ] * n
        self.DIFF_WEIGHT=[ 0 ] * n

    def root(self,x):
        if self.PAR[x] == x:
            return x
        else:
            r = self.root(self.PAR[x])
            self.DIFF_WEIGHT[x] += self.DIFF_WEIGHT[self.PAR[x]]
            self.PAR[x] = r
            return r
    
    def weight(self,x):
        self.root(x)
        return self.DIFF_WEIGHT[x]

    def issame(self,x,y):
        return self.root(x) == self.root(y)

    def diff(self,x,y):
        return self.weight(y)-self.weight(x)

    def merge(self,x,y,w):
        w += self.weight(x)
        w -= self.weight(y)
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.RANK[x] < self.RANK[y]:
            x,y = y,x
            w = -w
        if self.RANK[x] == self.RANK[y]:
            self.RANK[x] += 1

        self.PAR[y] = x
        self.DIFF_WEIGHT[y] = w
        return True


N,M  = map(int,input().split())
Ans = []
tree = WUnionFind(N+1)
b = True
for _ in range(M):
    l,r,d = map(int,input().split())
    if tree.issame(l,r) and tree.diff(l,r) != d:
        b = False
        break
    tree.merge(l,r,d)

if b:
    print('Yes')
else:
    print('No')