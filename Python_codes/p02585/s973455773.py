from math import log2
n,k=map(int,input().split())
p=list(map(int,input().split()))
c=list(map(int,input().split()))

k-=1

m=int(log2(k)) if 1<k else 1
nxt=[[0]*n for _ in range(m+1)]
point=[[0]*n for _ in range(m+1)]
for i in range(n):
  p[i]-=1
  nxt[0][i]=p[i]
  point[0][i]=c[p[i]]
for j in range(m):
  for i in range(n):
    nxt[j+1][i]=nxt[j][nxt[j][i]]
    point[j+1][i]=point[j][i]+point[j][nxt[j][i]]
min_nk=min(n,k)
ans=-10**18
for s in range(n):
  pla=p[s]
  cur=c[pla]
  if ans<cur:
    ans=cur
  for _ in range(min_nk):
    pla=p[pla]
    cur+=c[pla]
    if ans<cur:
      ans=cur
  if n<k:
    pla=p[s]
    cur=c[pla]
    for i in range(m+1):
      if (k-n)&(1<<i):
        cur+=point[i][pla]
        pla=nxt[i][pla]
    res=cur
    for _ in range(n):
      pla=p[pla]
      cur+=c[pla]
      if res<cur:
        res=cur
    if ans<res:
      ans=res
print(ans)