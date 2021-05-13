class Unionfind():
    def __init__(self,n):
        self.parents=[-1]*n
        self.ranks=[0]*n
    
    def find(self,x):
        if self.parents[x]<0:
            return x
        else:
            self.parents[x]=self.find(self.parents[x])
            return self.parents[x]
    
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
            return 
        if self.ranks[x]<self.ranks[y]:
            x,y=y,x
        self.parents[x]+=self.parents[y]
        self.parents[y]=x
        if self.ranks[x]==self.ranks[y]:
            self.ranks[x]+=1
    
    def number_of_class(self):
        return sum(x<0 for x in self.parents)
    
    def clear(self):
        self.parents=[-1]*n

n,m=map(int,input().split())
edge=[tuple(map(lambda x:int(x)-1,input().split())) for _ in range(m)]
g=Unionfind(n)
ans=0
for e in edge:
    g.clear()
    for f in edge:
        if f!=e:
            g.union(f[0],f[1])
    if g.number_of_class()>1:
        ans+=1
print(ans)
    
