N, M = map(int, input().split())
A = [True] * (N + 1)
for _ in range(M):
    a = int(input())
    A[a] = False

dp = [0] * (N + 1)

dp[0] = 1
for i in range(N):
    for j in range(i + 1, min(N, i + 2) + 1):
        if A[j] is True:
            dp[j] += dp[i]
            dp[j] %= 10 ** 9 + 7

print(dp[N])
