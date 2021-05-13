import sys
N,K=map(int, input().split())
mod=10**9+7
G={}
for i in range(N):
  G[i+1]=[]
for i in range(N-1):
  a,b=map(int, input().split())
  G[a].append(b)
  G[b].append(a)

for i in range(N):
  if len(G[i+1])>=K:
    print(0)
    exit()

def nPr(n,r):
  res=1
  for i in range(r):
    res*=(n-i)
    res%=mod
  return res

from collections import deque
q=deque([(1,0)])
ans=K
while q:
  n,m=q.pop()
  if m==0:
    ans*=nPr(K-1,len(G[n]))
    ans%=mod
    for d in G[n]:
      q.appendleft((d,n))
  else:
    ans*=nPr(K-2,len(G[n])-1)
    ans%=mod
    for d in G[n]:
      if d!=m:
        q.appendleft((d,n))
print(ans)