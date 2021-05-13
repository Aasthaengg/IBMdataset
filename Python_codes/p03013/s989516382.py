# C - Typical Stairs
N,M = map(int,input().split())
A = [int(input()) for _ in range(M)]
A = set(A)

# dp[i]: i 段目まで来た時の移動方法の総数
dp = [0]*(N+1)

# 初期条件
dp[0] = 1

for v in range(1,N+1):
    if v in A:
        continue
    dp[v] = (dp[v] + dp[v-1])%(1000000007)
    if v > 1:
        dp[v] = (dp[v] + dp[v-2])%(1000000007)
print(dp[N])