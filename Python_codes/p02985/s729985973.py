import sys

sys.setrecursionlimit(100000)

def dps(u,p,c):
  x[c]= u
  u = k-(1 if p<0 else 2)
  for i in range(len(l[c])):
    if l[c][i]!=p:
      if u>0:
        dps(u,c,l[c][i])
        u-=1
      else:
        break
  return

n,k=map(int,input().split())

l=[[] for i in range(n)]
x=[0]*n

for i in range(n-1):
  a,b= map(int,input().split())
  l[a-1].append(b-1)
  l[b-1].append(a-1)

dps(k,-1,0)

t=1
for i in range(n):
  t=(t*x[i])%(10**9+7)

print(t)
