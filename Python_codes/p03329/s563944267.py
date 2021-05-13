def main():
  N=int(input())
  values=[]
  val=6
  while val<=N:
    values.append(val)
    val*=6
  
  val=9
  while val<=N:
    values.append(val)
    val*=9
  values.append(1)
  values.sort()
  dp=[N]*(N+1)
  dp[0]=0
  for i in range(N):
    for v in values:
      if i+v>N:break
      dp[i+v]=min(dp[i]+1,dp[i+v])
  print(dp[N])
  pass
if __name__ == '__main__':
  main()
