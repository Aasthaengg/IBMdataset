class UnionFind():
  def __init__(self,n):
    self.n=n
    self.root=[-1]*(n+1)
    self.rank=[0]*(n+1)
  def FindRoot(self,x):
    if self.root[x]<0:
      return x
    else:
      self.root[x]=self.FindRoot(self.root[x])
      return self.root[x]
  def Unite(self,x,y):
    x=self.FindRoot(x)
    y=self.FindRoot(y)
    if x==y:
      return
    else:
      if self.rank[x]>self.rank[y]:
        self.root[x]+=self.root[y]
        self.root[y]=x
      elif self.rank[x]<=self.rank[y]:
        self.root[y]+=self.root[x]
        self.root[x]=y
        if self.rank[x]==self.rank[y]:
          self.rank[y]+=1
  def isSameGroup(self,x,y):
    return self.FindRoot(x)==self.FindRoot(y)
  def Count(self,x):
    return -self.root[self.FindRoot(x)]
  
n,k,l=map(int,input().split())
t1=UnionFind(n)
t2=UnionFind(n)
for _ in range(k):
  a,b=map(int,input().split())
  t1.Unite(a,b)
for _ in range(l):
  a,b=map(int,input().split())
  t2.Unite(a,b)
dic={}
for i in range(1,n+1):
  pos=(t1.FindRoot(i),t2.FindRoot(i))
  if pos not in dic:
    dic[pos]=1
  else:
    dic[pos]+=1
ans=[]
for i in range(1,n+1):
  pos=(t1.FindRoot(i),t2.FindRoot(i))
  ans.append(dic[pos])
print(*ans)