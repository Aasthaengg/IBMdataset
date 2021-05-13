import sys
input = sys.stdin.readline

S = input()[:-1]
dp = [[0]*4 for _ in range(len(S)+1)]
dp[0][0] = 1
MOD = 10**9+7

for i in range(len(S)):
    dp[i+1][0] = dp[i][0]*(3 if S[i]=='?' else 1)%MOD
    dp[i+1][1] = (dp[i][1]*(3 if S[i]=='?' else 1)+(dp[i][0] if S[i] in ['A', '?'] else 0))%MOD
    dp[i+1][2] = (dp[i][2]*(3 if S[i]=='?' else 1)+(dp[i][1] if S[i] in ['B', '?'] else 0))%MOD
    dp[i+1][3] = (dp[i][3]*(3 if S[i]=='?' else 1)+(dp[i][2] if S[i] in ['C', '?'] else 0))%MOD
    
print(dp[-1][3])