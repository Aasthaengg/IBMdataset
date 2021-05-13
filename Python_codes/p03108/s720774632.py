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
N,M=map(int,input().split())
uf=UnionFind(N)
AB=[]
for i in range(M):
  AB.append(list(map(int,input().split())))
ans=[0]*M
ans[M-1]=(N*(N-1))//2
for i in range(M-2,-1,-1):
  if uf.isSameGroup(AB[i+1][0],AB[i+1][1]):
    ans[i]=ans[i+1]
  else:
    n1=uf.Count(AB[i+1][0])
    n2=uf.Count(AB[i+1][1])
    ans[i]=ans[i+1]-n1*n2
  uf.Unite(AB[i+1][0],AB[i+1][1])
for i in range(M):
  print(ans[i])