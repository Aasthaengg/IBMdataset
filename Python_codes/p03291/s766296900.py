s=input()
n=len(s)
dp=[[0 for i in range(4)]for j in range(n+1)]
for i in range(n,-1,-1):
  for j in range(3,-1,-1):
    if i==n:
      if j==3:
        dp[i][j]=1
      else:
        dp[i][j]=0
    else:
      if j==3:
        if s[i]=='?':
          dp[i][j]=dp[i+1][j]*3
        else:
          dp[i][j]=dp[i+1][j]
      else:
        if s[i]=='?':
          dp[i][j]=dp[i+1][j]*3+dp[i+1][j+1]
        elif (j==0 and s[i]=='A') or (j==1 and s[i]=='B') or (j==2 and s[i]=='C'):
          dp[i][j]=dp[i+1][j]+dp[i+1][j+1]
        else:
          dp[i][j]=dp[i+1][j]
    dp[i][j]%=10**9+7
print(dp[0][0])