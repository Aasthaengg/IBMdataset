class UnionFind():
    def __init__(self,n):
        self.n=n
        self.root=[-1]*(n+1)
        self.rnk=[0]*(n+1)

    def Find_Root(self,x):
        if self.root[x]<0:
            return x
        else:
            self.root[x]=self.Find_Root(self.root[x])
            return self.root[x]

    def Unite(self,x,y):
        x=self.Find_Root(x)
        y=self.Find_Root(y)
        if x==y:
            return
        elif self.rnk[x]>self.rnk[y]:
            self.root[x]+=self.root[y]
            self.root[y]=x
        else:
            self.root[y]+=self.root[x]
            self.root[x]=y
            if self.rnk[x]==self.rnk[y]:
                self.rnk[y]+=1

    def isSameGroup(self,x,y):
        return self.Find_Root(x)==self.Find_Root(y)

    def Count(self,x):
        return -self.root[self.Find_Root(x)]

h,w=map(int,input().split())
g=[list(input()) for _ in range(h)]
uf=UnionFind(h*w)
dyx=[(1,0),(-1,0),(0,1),(0,-1)]
for i in range(h):
    for j in range(w):
        if g[i][j]==".":
            continue
        p=i*w+j
        for dy,dx in dyx:
            y=i+dy
            x=j+dx
            if 0<=y<h and 0<=x<w:
                if g[y][x]==".":
                    np=y*w+x
                    uf.Unite(p,np)

rt=[0]*(h*w)
for i in range(h*w):
    rt[i]=uf.Find_Root(i)

m=min(rt)
rt=list(map(lambda x:x-m, rt))
m=max(rt)
a=[[0,0] for _ in range(m+1)]
for i in range(h*w):
    y=i//w
    x=i%w
    if g[y][x]=="#":
        a[rt[i]][0]+=1
    else:
        a[rt[i]][1]+=1
ans=0
for i,j in a:
    ans+=i*j

print(ans)
