class uft():
    def __init__(self,n):
        self.p=[ -1 for i in range(n)]
        self.r=[ 1 for i in range(n)]
        
    def find(self,x):
        if(self.p[x]==-1):
            return x
        else:
            self.p[x]=self.find(self.p[x])
            return self.find(self.p[x])
        
    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if(self.r[x]>self.r[y]):
            tmp=x
            x=y
            y=tmp
            
        if(self.r[x]==self.r[y]):
            self.r[y]+=1
            
        if(x!=y):
            self.p[x]=y
        return
    
n,m=map(int,input().split())
p=list(map(int,input().split()))
for i in range(n):
  p[i]-=1
uf=uft(n)
for i in range(m):
    x,y=map(int,input().split())
    x-=1
    y-=1
    uf.unite(x,y)
ans=0
for i in range(n):
    if(uf.find(i)==uf.find(p[i])):
        ans+=1
        
print(ans)