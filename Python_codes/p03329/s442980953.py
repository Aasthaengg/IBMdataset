import sys
n = int(input())
INF = 10*n
dp = [INF]*(n+1)
dp[0] = 0
for i in range(1, n+1):
    tmp = dp[i-1] + 1
    for j in range(10):
        if i-6**j<0:
            break
        tmp = min(tmp, dp[i-6**j] + 1)
    for j in range(10):
        if i-9**j<0:
            break
        tmp = min(tmp, dp[i-9**j] + 1)
    dp[i] = tmp
print(dp[n])