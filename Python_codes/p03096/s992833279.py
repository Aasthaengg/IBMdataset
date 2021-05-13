# 解説 https://betrue12.hateblo.jp/entry/2019/03/17/011847
# from collections import defaultdict

mod = 10 ** 9 + 7

N = int(input())
C = [int(input()) for _ in range(N)]
# L = [-1] * (N + 10)  # 出たところ
# dp = [-1] * (N + 10)
# dp[0] = 1
L  = [-1] * (2*10**5 + 10)
dp = [-1] * (2*10**5 + 10)
dp[0] = 1
 

for i in range(N):
    if L[C[i]] == -1:
        dp[i + 1] = dp[i]
    elif C[i] == C[i - 1]:
        dp[i + 1] = dp[i]
    else:
        dp[i + 1] = dp[i] + dp[L[C[i]]]
    
    dp[i + 1] %= mod
    L[C[i]] = i + 1

print(dp[N])
