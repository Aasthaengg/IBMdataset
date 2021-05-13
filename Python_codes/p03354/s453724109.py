class uf():
    def __init__(self,n):
        self.n=n
        self.pa=[-1]*n
    def find(self,x):
        if self.pa[x]<0:
            return x
        else:
            self.pa[x]=self.find(self.pa[x])
            return self.pa[x]
    def unite(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y:
        	return True
        else:
            if self.pa[x]>self.pa[y]:
                x,y=y,x
            self.pa[x]+=self.pa[y]
            self.pa[y]=x
            return True
    def same(self,x,y):
        return self.find[x]==find.pa[y]
    def size(self,x):
        return -self.pa[self.find(x)] 
n,m=map(int,input().split())
import sys
input=sys.stdin.readline
l=list(map(int,input().split()))
uf=uf(n)
for i in range(m):
    a,b=map(int,input().split())
    uf.unite(a-1,b-1)
d=dict()
for i in range(n):
    if uf.find(i) in d:
        d[uf.find(i)].add(i)
    else:
        d[uf.find(i)]=set([i])
for x in d:
  for y in d[x]:
    if l[y]-1 in d[x]:
      pass
    else:
      n-=1
print(n)