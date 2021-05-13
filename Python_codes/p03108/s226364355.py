class UnionFind():
  def __init__(self, n=10**6):
    self.n=n
    self.root=[-1]*(n+1)
    self.rnk=[0]*(n+1)
  def find(self, x):
    if(self.root[x]<0):
      return x
    else:
      self.root[x]=self.find(self.root[x])
      return self.root[x]
  def unite(self, x, y):
    x=self.find(x)
    y=self.find(y)
    if(x==y):return 
    elif(self.rnk[x] > self.rnk[y]):
      self.root[x]+=self.root[y]
      self.root[y]=x
    else:
      self.root[y]+=self.root[x]
      self.root[x]=y
      if(self.rnk[x]==self.rnk[y]):
        self.rnk[y]+=1
  def same(self, x, y):
    return self.find(x)==self.find(y)
  def count(self, x):
    return -self.root[self.find(x)]
n,m=map(int,input().split())
uf=UnionFind(n)
a=[0]*m
b=[0]*m
for i in range(m):
  a[i],b[i]=map(int,input().split())
c=[1]*(n+1)
ans=[]
nm=n*(n-1)//2
for i in range(m-1,-1,-1):
  ans+=[nm]
  x,y=a[i],b[i]
  if uf.same(x,y):continue
  nm-=uf.count(x)*uf.count(y)
  uf.unite(x,y)
print(*ans[::-1],sep='\n')