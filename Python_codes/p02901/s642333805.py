def main():
  n,m=map(int,input().split())
  inf=10**9
  dp=[inf]*(1<<n)
  dp[0]=0
  for i in range(m):
    a,b=map(int,input().split())
    t=sum([1<<(int(x)-1) for x in input().split()])
    for s in range(1<<n):
      dp[t|s]=dp[t|s] if dp[t|s]<=dp[s]+a else dp[s]+a
  print(-1 if dp[-1]==inf else dp[-1])
  
  
if __name__=='__main__':
  main()
