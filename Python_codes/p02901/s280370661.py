N, M = map(int, input().split())
BIT = 2 ** N
dp =[[float("inf") for _ in range(BIT)] for _ in range(M + 1)]
dp[0][0] = 0

for i in range(M):
    A, B = map(int, input().split())
    C = list(map(int, input().split()))
    x = sum([2 ** (c - 1) for c in C])
    for j in range(BIT):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        dp[i + 1][x|j] = min(dp[i][j] + A, dp[i + 1][x|j])

ans = dp[M][BIT - 1]
if ans != float("inf"):
    print(ans)
else:
    print(-1)