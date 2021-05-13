n,m=map(int,input().split())
edge=[[] for i in range(n)]
kara=[]
to=[0]*n
for i in range(m):
  x,y=map(int,input().split())
  edge[x-1].append(y-1)
  to[y-1]+=1
for j in range(n):
  if to[j]==0:
    kara.append(j)
dp=[0]*n
while len(kara):
  go=kara.pop()
  for e in edge[go]:
    to[e]-=1
    if to[e]==0:
      kara.append(e)
    dp[e]=max(dp[e],dp[go]+1)
print(max(dp))