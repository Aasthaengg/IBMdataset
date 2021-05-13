import sys
input = sys.stdin.readline

S = input()[:-1]
dp = [[0]*2 for _ in range(len(S))]
dp[0][0] = 1
dp[1][1] = 1

for i in range(len(S)):
    if i>=1 and S[i]!=S[i-1]:
        dp[i][0] = max(dp[i][0], dp[i-1][0]+1)
    
    if i>=1:
        dp[i][0] = max(dp[i][0], dp[i-1][1]+1)
        
    if i>=2:
        dp[i][1] = max(dp[i][1], dp[i-2][0]+1)
    
    if i>=2 and S[i-3:i-1]!=S[i-1:i+1]:
        dp[i][1] = max(dp[i][1], dp[i-2][1]+1)

print(max(dp[-1]))