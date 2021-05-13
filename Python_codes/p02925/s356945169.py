import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def main():
  n=int(input())
  a=[list(map(int,input().split())) for _ in range(n)]
  f=lambda x:((x[0]-1)*(n-1+n-x[0]+1))//2+x[1]-x[0]-1
  m=(n*(n-1))//2
  g=[[] for _ in range(m)]
  for i in range(n):
    for j in range(n-2):
      if i+1>a[i][j]:
        t0=f((a[i][j],i+1))
      else:
        t0=f((i+1,a[i][j]))
      if i+1>a[i][j+1]:
        t1=f((a[i][j+1],i+1))
      else:
        t1=f((i+1,a[i][j+1]))
      g[t0].append(t1)
  def dfs(t):
    if v[t]:
      if c[t]==0:
        return -1
      else:
        return dp[t]
    v[t]=1
    for l in g[t]:
      ret=dfs(l)
      if ret==-1:return -1
      dp[t]=max(dp[t],ret+1)
    c[t]=1
    mi.discard(t)
    return dp[t]
  ans=0
  v=[0]*m
  c=[0]*m
  dp=[0]*m
  #print(g)
  mi=set(list(range(m)))
  while mi:
    i=mi.pop()
    tmp=dfs(i)
    if tmp==-1:
      print(-1)
      exit()
    ans=max(ans,tmp)
    #print(dp)
  print(ans+1)

if __name__=='__main__':
  main()
