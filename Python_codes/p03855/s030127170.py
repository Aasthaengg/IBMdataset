N,K,L=map(int,input().split())

class UnionFind():
  def __init__(self,N):
    self.parents=list(range(N))
    self.size=[1]*N
  def find(self,x):
    if self.parents[x]==x:
      return x
    else:
      self.parents[x]=self.find(self.parents[x])
      return self.parents[x]
  def union(self,x,y):
    x,y=self.find(x),self.find(y)
    if x==y:
      return 
    if self.size[x]<self.size[y]:
      self.size[y]+=self.size[x]
      self.parents[x]=y
    else:
      self.size[x]+=self.size[y]
      self.parents[y]=x

uf1=UnionFind(N)
uf2=UnionFind(N)
for i in range(K):
  x,y=map(int,input().split())
  uf1.union(x-1,y-1)
for j in range(L):
  x,y=map(int,input().split())
  uf2.union(x-1,y-1)

keys=[(uf1.find(x),uf2.find(x)) for x in range(N)]
count={}
for key in keys:
  if key in count:
    count[key]+=1
  else:
    count[key]=1
print(*[count[key] for key in keys])