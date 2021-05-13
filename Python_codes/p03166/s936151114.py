import sys
sys.setrecursionlimit(2000000000)
n,m=map(int,input().split())
v=[[] for i in range(n)]
for i in range(m):
  a,b=map(int,input().split())
  v[a-1].append(b-1)

memo=[-1]*n
def dp(x):
  if memo[x]!=-1:return memo[x]
  r=0
  for i in v[x]:
    r=max(r,dp(i)+1)
  memo[x]=r
  return r
print(max(dp(i) for i in range(n)))