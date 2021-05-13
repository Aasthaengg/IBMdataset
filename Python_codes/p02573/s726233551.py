class uft():
    def __init__(self,n):
        #pは代表元か-1
        self.p=[ -1 for i in range(n)]
        #ランク　木の深さ
        self.r=[ 1 for i in range(n)]
        #要素数
        self.e=[ 1 for i in range(n)]
        
    def find(self,x):
        if(self.p[x]==-1):
            return x
        else:
            self.p[x]=self.find(self.p[x])
            return self.find(self.p[x])
        
    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if(x==y):
            return
        
        if(self.r[x]>self.r[y]):
            tmp=x
            x=y
            y=tmp
        
        if(self.r[x]==self.r[y]):
            self.r[y]+=1
        
        self.e[y]+=self.e[x]
            
        if(x!=y):
            self.p[x]=y
        return
    
    def tsize(self,x):
        return self.e[self.find(x)]
n,m=map(int,input().split())

uf=uft(n)
for i in range(m):
    x,y=map(int,input().split())
    x-=1
    y-=1
    uf.unite(x,y)
ans=0
for i in range(n):
    ans=max(ans,uf.tsize(i))
print(ans)