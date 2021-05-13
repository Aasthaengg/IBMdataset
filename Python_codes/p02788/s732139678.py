from collections import*
INF=10**18
n,d,a=map(int,input().split())
mon=[]
for _ in range(n):
  mon+=[list(map(int,input().split()))]
mon.sort()
ans=0
tot=0
q=deque()
for i in range(n):
  x,h=mon[i]
  while q and q[0][0]<x:
    tot-=q.popleft()[1]
  h-=tot
  if h>0:
    b=(h+a-1)//a
    tot+=b*a
    ans+=b
    q.append((x+2*d,b*a))
print(ans)