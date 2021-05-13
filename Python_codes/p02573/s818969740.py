n,m=map(int,input().split())

P=[-1]*n

def find(x):
  if P[x]<0:
    return x
  P[x]=find(P[x])
  return P[x]

def unite(x,y):
  x=find(x)
  y=find(y)
  if x==y:
    return

  if P[x]>P[y]:
    P[y]+=P[x]
    P[x]=y
  else:
    P[x]+=P[y]
    P[y]=x

def size(x):
  return -P[find(x)]

for i in range(m):
  a,b=map(int,input().split())
  unite(~-a,~-b)

print(-min(P))
