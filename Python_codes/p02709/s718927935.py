N = int(input())
A = map(int, input().split())

B = [[i, a] for i, a in enumerate(A)]

C = sorted(B, key=lambda b: b[1], reverse=True)

dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]

dp[1][0] = (C[0][0] - 0) * C[0][1]
dp[0][1] = ((N - 1) - C[0][0]) * C[0][1]

ans = 0
for i in range(2, N + 1):
    for j in range(0, i + 1):
        t1, t2 = 0, 0

        if j - 1 >= 0:
            t1 = dp[j - 1][i - j] + abs((C[i - 1][0] - (j - 1))) * C[i - 1][1]

        if i - j - 1 >= 0:
            t2 = dp[j][i - j - 1] + abs((C[i - 1][0] - (N - (i - j)))) * C[i - 1][1]

        dp[j][i - j] = max(t1, t2)

        if i == N:
            ans = max(ans, dp[j][i - j])

print(ans)
