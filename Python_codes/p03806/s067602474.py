N, Ma, Mb = map(int, input().split())
a = [0] * N
b = [0] * N
c = [0] * N
for i in range(N):
    a[i], b[i], c[i] = map(int, input().split())

INF = 10 ** 5
nums = 401

dp = [[[INF for _ in range(nums)] for _ in range(nums)] for _ in range(N+1)]

dp[0][0][0] = 0

for i in range(N):
    for sum_a in range(nums):
        for sum_b in range(nums):
            if dp[i][sum_a][sum_b] == INF:
                continue
            dp[i+1][sum_a][sum_b] = min(dp[i+1][sum_a][sum_b], dp[i][sum_a][sum_b])
            dp[i+1][sum_a+a[i]][sum_b+b[i]] = min(dp[i+1][sum_a+a[i]][sum_b+b[i]], dp[i][sum_a][sum_b] + c[i])
            # print(i, dp[i][sum_a][sum_b], sum_a, sum_b)


res = INF
for i in range(1, nums):
    for j in range(1, nums):
        if i * Mb == j * Ma:
            res = min(res, dp[N][i][j])

if res == INF:
    res = -1

print(res)
