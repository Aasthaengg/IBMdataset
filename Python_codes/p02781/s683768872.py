n=[int(x) for x in list(input())]
l=len(n)
k=int(input())
"""
桁DP
桁数,0でないcount,ギリギリflagでdp
"""
dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(l+1)]
#n[0]は0ではない
dp[1][0][0] = 1
dp[1][1][0] = n[0] - 1
dp[1][1][1] = 1
for i in range(2,l+1):
  for j in range(0,min(i,k)+1):
    if j > 0:
      dp[i][j][1] += dp[i-1][j-1][1]*(n[i-1]>0)
      dp[i][j][0] += dp[i-1][j-1][0]*9+dp[i-1][j-1][1]*max(0,n[i-1]-1)
    dp[i][j][1] += dp[i-1][j][1]*(n[i-1]==0)
    dp[i][j][0] += dp[i-1][j][0] + dp[i-1][j][1]*(n[i-1]>0)
    #print(i,j,dp[i][j])
print(sum(dp[l][k]))