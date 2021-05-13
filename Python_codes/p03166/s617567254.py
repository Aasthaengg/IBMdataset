import sys
sys.setrecursionlimit(10**7)

def dfs(x):
  if x in memo:
    return memo[x]
  ret=0
  for y in g[x]:
    ret=max(ret,dfs(y)+1)
  memo[x]=ret
  return ret

n,m=map(int,input().split())
g=[[] for _ in range(n+1)]
for _ in range(m):
  a,b=map(int,input().split())
  g[a].append(b)
memo={}
for i in range(1,n+1):
  dfs(i)
print(max(memo.values()))