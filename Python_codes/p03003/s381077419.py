N,M=map(int,input().split())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
MOD=10**9+7
dp=[]
for i in range(len(s)+1):
  dp.append([0]*(len(t)+1))
for i in range(len(s)):
  for j in range(len(t)):
    if s[i] == t[j]: 
      dp[i+1][j+1] = (dp[i+1][j]+dp[i][j+1]+1)%MOD
    else:
      dp[i+1][j+1] = dp[i+1][j]+dp[i][j+1]-dp[i][j]
print((dp[len(s)][len(t)]+1)%MOD)