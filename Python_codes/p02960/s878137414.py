#template
def inputlist(): return [int(k) for k in input().split()]
#template
mod = 10**9+7
S = list(input())
n = len(S)
#桁dp
dp = [[0]*(13) for _ in range(n+1)]
if S[0] == '?':
    for i in range(10):
        dp[1][i] = 1
if S[0] != '?':
    dp[1][int(S[0])] = 1
for i in range(1,n):
    i+=1
    if S[i-1] == '?':
        for m in range(13):
            for j in range(10):
                dp[i][(10*m+j)%13] += dp[i-1][m]
                dp[i][(10*m+j)%13] %= mod
        continue
    if S[i-1] != '?':
        for m in range(13):
            dp[i][(10*m+int(S[i-1]))%13] += dp[i-1][m]
            dp[i][(10*m+int(S[i-1]))%13] %= mod
dp[n][5] %= mod
print(dp[n][5])