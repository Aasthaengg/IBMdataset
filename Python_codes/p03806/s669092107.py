inf = float("inf")
N, Ma, Mb = map(int, input().split())
ABC = []
for _ in range(N):
    a, b, c = map(int, input().split())
    ABC.append((a, b, c))
dp = [[inf] * 420 for _ in range(420)]
dp[0][0] = 0
for a, b, c in ABC:
    for i in range(410, -1, -1):
        for j in range(410, -1, -1):
            if dp[i][j] < inf:
                dp[i+a][j+b] = min(dp[i+a][j+b], dp[i][j] + c)
ans = inf
n = 1
while max(Ma * n, Mb * n) < 420:
    ans = min(ans, dp[Ma * n][Mb * n])
    n += 1
print(ans if ans < inf else -1)
