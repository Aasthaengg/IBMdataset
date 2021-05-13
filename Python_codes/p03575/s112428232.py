#dfs renshuu
from collections import defaultdict

def dfs(x):
  if f[x] == 1: return
  f[x]=1
  for nex in dd[x]:
    if x==a and nex==b: continue
    dfs(nex)

n,m=map(int,input().split())
dd=defaultdict(list)
lst=[]
ans=0
for i in range(m):
  a,b=map(int,input().split())
  lst.append((a,b,))
  dd[a].append(b)
  dd[b].append(a)
for a,b in lst:
  f=[0]*(n+1)
  dfs(a)
  if f[b]!=1:
    ans+=1
print(ans)
