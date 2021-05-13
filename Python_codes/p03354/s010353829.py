import sys
from collections import defaultdict
import bisect
sys.setrecursionlimit(1000000)
d1=defaultdict(list)
d2=defaultdict(list)
n,m=map(int,input().split())
l=list(map(int,input().split()))
la=[[] for i in range(n+1)]
for i in range(m):
  a,b=map(int,input().split())
  la[a].append(b)
  la[b].append(a)
lb=[0 for i in range(n+1)]
def dfs(x,y):
  if lb[x]!=0:
    return
  else:
    lb[x]=y
    s=la[x]
    if s==[]:
      pass
    else:
      for i in s:
        dfs(i,y)
c=1
for i in range(1,n+1):
  dfs(i,c)
  c+=1
lc=set(lb)
for i in range(1,n+1):
  d1[lb[i]]+=[i]
  d2[lb[i]]+=[l[i-1]]
ans=0
for i in d1:
  d11=d1[i]
  d12=d2[i]
  for j in d12:
    index=bisect.bisect_right(d11,j)
    if d11[index-1]==j:
      ans+=1
print(ans)