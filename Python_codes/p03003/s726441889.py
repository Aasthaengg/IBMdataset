# coding: utf-8
# Your code here!

N, M = list(map(int, input().rstrip().split(' ')))
S = list(map(int, input().rstrip().split(' ')))
T = list(map(int, input().rstrip().split(' ')))
dp = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        if S[j-1] == T[i-1]:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] + 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        dp[i][j] = dp[i][j] % 1000000007
            
print((dp[-1][-1]+1) % 1000000007)
