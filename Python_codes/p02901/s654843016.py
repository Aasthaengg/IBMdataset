N, M = map(int, input().split())

dp =[[float("inf") for _ in range(2 ** N)] for _ in range(M + 1)]
dp[0][0] = 0

for i in range(M):
    A, B = map(int, input().split())
    C = list(map(int, input().split()))
    tmp = [0 for _ in range(N)]
    for c in C:
        tmp[c - 1] = 1
    x = int("".join(map(str, tmp)), 2)
    for j in range(2 ** N):
        dp[i + 1][x|j] = min(dp[i][x|j], dp[i][j] + A, dp[i + 1][x|j])
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])

ans = dp[M][2 ** N - 1]
if ans != float("inf"):
    print(ans)
else:
    print(-1)