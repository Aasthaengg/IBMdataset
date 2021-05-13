import sys
sys.setrecursionlimit(10000000)
n,k=map(int,input().split())
graph=[[] for i in range(n)]
for i in range(n-1):
  a,b=map(int,input().split())
  graph[a-1].append(b-1)
  graph[b-1].append(a-1)
MOD=10**9+7
def coloring(node,pre):
  if len(graph[node])>k:
    return 0
  if pre==-1:
    color=k-1
  else:
    color=k-2
  ans=1
  for i in graph[node]:
    if i==pre:continue
    ans*=color
    ans%=MOD
    color-=1
  for i in graph[node]:
    if i==pre:continue
    ans*=coloring(i,node)
    ans%=MOD
  return ans
print((k*coloring(0,-1))%MOD)
