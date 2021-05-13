N = int(input())
A = list(map(int, input().split()))

# dp[i][j]：A_1,...,A_iを確定させ, A_iの符号をj回反転させたときの
# Aの和の最大値

INF = float('inf')
dp = [[-INF]*2 for _ in range(N+1)]
dp[0][0] = 0
for i in range(N):
    for j in range(2):
        dp[i+1][j] = max(dp[i][0]+A[i]*(-1)**j, dp[i][1]-A[i]*(-1)**j)
print(dp[N][0])