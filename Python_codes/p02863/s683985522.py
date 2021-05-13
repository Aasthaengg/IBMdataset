N, T = map(int, input().split())
D = [tuple(map(int, input().split())) for _ in range(N)]
D.sort()
dp = [[0] * T for _ in range(N + 1)]

for i in range(N):
    A, B = D[i]
    for j in range(T):
        here = dp[i][j]
        if j < A:
            dp[i + 1][j] = here
        else:
            dp[i + 1][j] = max(here, dp[i][j - A] + B)

t = 0
ans = 0
for i in range(N - 1, -1, -1):
    ans = max(ans, dp[i + 1][T - 1] + t)
    t = max(t, D[i][1])

print(ans)
