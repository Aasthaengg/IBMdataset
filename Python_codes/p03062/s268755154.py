N = int(input())
A = list(map(int,input().split()))

dp = [[0] * 2 for _ in range(N+1)]#dp[i][0] = A1からAiの最大値(Ai+1は反転なし)

dp[0][0] = 0
dp[0][1] = -float("inf")

for i in range(N):
    dp[i+1][0] = max(dp[i][0] + A[i], dp[i][1] - A[i])
    dp[i+1][1] = max(dp[i][0] - A[i], dp[i][1] + A[i])
print(dp[N][0])