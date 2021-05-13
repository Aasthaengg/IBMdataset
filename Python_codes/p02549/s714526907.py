import sys

input = sys.stdin.readline

N, K = map(int, input().split())
LR = [list(map(int, input().split())) for i in range(K)]
MOD = 998244353
 
dp = [0] * (N + 1)
dp[1] = 1
dp_sum = [0] * (N + 1)
dp_sum[1] = 1
 
 
def get(l, r, i):
    return dp_sum[max((i - l), 0)] - dp_sum[max((i - r-1), 0)]
 
 
for i in range(1, N+1):
    for l, r in LR:
        dp[i] += get(l, r, i) % MOD
    dp_sum[i] = (dp_sum[i - 1] + dp[i])%MOD

print(dp[N] % MOD)