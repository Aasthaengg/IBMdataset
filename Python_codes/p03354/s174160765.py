class UnionFind():
    def __init__(self,n):
        self.n=n
        self.par=[i for i in range(n)]
        self.size=[0 for i in range(n)]
    def find(self,x):
        if x==self.par[x]:
            return x
        self.par[x]=self.find(self.par[x])
        return self.par[x]
    def merge(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return
        if self.size[x]>=self.size[y]:
            self.par[y]=x
            self.size[x]+=self.size[y]
        else:
            self.par[x]=y
            self.size[y]+=self.size[x]
    def same(self,x,y):
        x=self.find(x)
        y=self.find(y)
        return x==y
n,m=map(int,input().split())
p=list(map(int,input().split()))
uf=UnionFind(n)
for _ in range(m):
    x,y=map(int,input().split())
    uf.merge(x-1,y-1)
ans=0
for i in range(n):
    if p[i]-1==i or uf.same(i,p[i]-1):
        ans+=1
print(ans)
