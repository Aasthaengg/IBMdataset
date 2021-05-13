class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*n
        self.rank = [0]*n

    def find(self, x):
        if self.root[x-1] < 0:
            return x
        else:
            self.root[x-1] = self.find(self.root[x-1])
            return self.root[x-1]

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        elif self.rank[x-1] > self.rank[y-1]:
            self.n-=1
            self.root[x-1] += self.root[y-1]
            self.root[y-1] = x
        else:
            self.n-=1
            self.root[y-1] += self.root[x-1]
            self.root[x-1] = y
            if self.rank[x-1] == self.rank[y-1]:
                self.rank[y-1] += 1

    def same(self, x, y):
        return self.find(x)==self.find(y)

    def count(self, x):
        return -self.root[self.find(x)-1]

    def size(self):
        return self.n

N,M=map(int,input().split())
B=[tuple(map(int,input().split())) for i in range(M)]
s=N*(N-1)//2
ans=[0]*M
uf=UnionFind(N)
for i in range(M-1,-1,-1):
    ans[i]=s
    a,b=B[i]
    if uf.find(a)!=uf.find(b):
        t1,t2=uf.count(a),uf.count(b)
        uf.unite(a,b)
        s-=(t1+t2)*(t1+t2-1)//2-(t1*(t1-1)//2+t2*(t2-1)//2)
print(*ans,sep='\n')