N,K=map(int,input().split())
Tree=[[] for i in range(N)]
MOD=10**9+7
import sys
sys.setrecursionlimit(10**9)
for i in range(N-1):
  a,b=map(int,input().split())
  Tree[a-1].append(b-1)
  Tree[b-1].append(a-1)
def P(n,m):
  _=n
  for i in range(m-1):
    n-=1
    _*=n
    _%=MOD
  return _%MOD
def dfs(p,i):
  global Tree,ans
  n=len(Tree[i])-1
  if n==0:
    return
  if i==0:
    ans*=P(K-1,n)
  else:
    ans*=P(K-2,n)
    ans%=MOD
  for j in Tree[i]:
    if j==p:
      continue
    dfs(i,j)
Tree[0].append(-1)
ans=K
dfs(-1,0)
print(ans%MOD)