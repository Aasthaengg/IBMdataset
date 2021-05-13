def main():
  n=int(input())
  s=input()
  dp=[[0]*(n+1) for i in range(n+1)]
  for i in reversed(range(n)):
    for j in reversed(range(i+1,n)):
      if s[i]==s[j]:
        dp[i][j]=dp[i+1][j+1]+1
  
  ans=0
  for i in range(n):
    for j in range(i+1,n):
      ans=max(ans,min(j-i,dp[i][j]))
  print(ans)
        

if __name__=='__main__':
  main()