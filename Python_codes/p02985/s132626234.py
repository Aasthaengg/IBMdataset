import sys
sys.setrecursionlimit(10**6)
n,k=map(int,input().split())
l=[[] for i in range(n+1)]
for i in range(n-1):
  a,b=map(int,input().split())
  l[a].append(b)
  l[b].append(a)
ans=[k]
mod=10**9+7
def dfs(s,p):#sは今いる点colはその点の色
  if s==1:
    now=k-1
  else:
    now=k-2
  for i in l[s]:
    if i==p:
      pass
    else:
      ans[0]=(ans[0]*now)%mod
      now-=1
      dfs(i,s)
dfs(1,0)
print(ans[0])