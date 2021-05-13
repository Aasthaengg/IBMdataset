from numpy import zeros

N = int(input())
P = map(float, input().split())

dp = zeros(N + 1)
dp[0] = 1.0

for p in P:
    T = dp
    dp = T * (1 - p)
    dp[1:] += T[:-1] * p

print(dp[-(-N // 2):].sum())