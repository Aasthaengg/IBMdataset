import collections
import sys
input = sys.stdin.readline
n,k,l=map(int,input().split())

parD,parT=[-1]*n,[-1]*n
def findD(x):
  if parD[x]<0:
    return x
  else:
    parD[x]=findD(parD[x])
    return parD[x]
def uniteD(x,y):
  x=findD(x)
  y=findD(y)
  if x==y:
    return False
  else:
    if parD[x]>parD[y]:
      x,y=y,x
    parD[x]+=parD[y]
    parD[y]=x
    return True
def sameD(x,y):
  return findD(x)==findD(y)
def sizeD(x):
  return -parD[findD(x)]
def findT(x):
  if parT[x]<0:
    return x
  else:
    parT[x]=findT(parT[x])
    return parT[x]
def uniteT(x,y):
  x=findT(x)
  y=findT(y)
  if x==y:
    return False
  else:
    if parT[x]>parT[y]:
      x,y=y,x
    parT[x]+=parT[y]
    parT[y]=x
    return True
def sameT(x,y):
  return findT(x)==findT(y)
def sizeD(x):
  return -parT[findT(x)]


for i in range(k):
  p,q=map(int,input().split())
  uniteD(p-1,q-1)
for i in range(l):
  r,s=map(int,input().split())
  uniteT(r-1,s-1)
for i in range(n):
  findD(i)
  findT(i)
C=[]
for i in range(n):
  if parD[i]<0:
    parD[i]=i
  if parT[i]<0:
    parT[i]=i
Ans=[]
for i in range(n):
  Ans.append((parD[i],parT[i]))
ANS=collections.Counter(Ans)
for i in range(n):
  print(ANS[Ans[i]])