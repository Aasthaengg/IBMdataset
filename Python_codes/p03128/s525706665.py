N, M, *A = map(int, open(0).read().split())

C = [0, 1, 4, 4, 3, 4, 5, 2, 6, 5]

dp = [0] * N + [-1] * 9
for i in range(N):
    dp[i + 1] = max(a + 10 * dp[i - C[a]] for a in A)

print(dp[N])
