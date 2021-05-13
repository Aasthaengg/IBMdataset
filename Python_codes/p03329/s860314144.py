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
  
  values.sort(reverse=True)
  dp=[N]*(N+1)
  dp[0]=0
  for value in values:
    for i in range(0,N-value+1):
      if dp[i] != N:
        dp[i+value]=min(dp[i]+1,dp[i+value])
        #print(i,value,dp[i+value])
  #print(dp)
  ans=10**10
  for index,item in enumerate(dp):
    ans=min(ans,item+N-index)
  print(ans)
  pass
if __name__ == '__main__':
  main()