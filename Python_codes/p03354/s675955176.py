import sys
input = sys.stdin.readline
class UnionFind:
  def __init__(self,nodes):
    self.parents={node: node for node in nodes}
  def root(self,x):
    if x==self.parents[x]:
      return x
    else:
      rt=self.root(self.parents[x])
      self.parents[x]=rt
      return rt
  def find(self,x,y):
    return self.root(x)==self.root(y)
  def union(self,x,y):
    self.parents[self.root(x)]=self.root(y)

n,m=map(int,input().split())
P=list(map(int,input().split()))
uf=UnionFind(range(1,n+1))
for i in range(m):
  x,y=map(int,input().split())
  uf.union(x,y)
  
ans=0
for i in range(1,n+1):
  if uf.find(i,P[i-1]):
    ans+=1
print(ans)