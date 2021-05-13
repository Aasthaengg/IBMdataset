N, Ma, Mb = map(int, input().split())
info = []
a_list = [0] * N
b_list = [0] * N
c_list = [0] * N
for i in range(N):
    a, b, c = map(int, input().split())
    a_list[i] = a
    b_list[i] = b
    c_list[i] = c

inf = 10 ** 10
a_sum = sum(a_list)
b_sum = sum(b_list)
dp = [[[inf for _ in range(b_sum + 1)] for _ in range(a_sum + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
    a, b, c = a_list[i], b_list[i], c_list[i]
    for j in range(a_sum + 1):
        for k in range(b_sum + 1):
            if j - a >= 0 and k - b >= 0:
                dp[i + 1][j][k] = min(dp[i][j - a][k - b] + c, dp[i][j][k])
            else:
                dp[i + 1][j][k] = dp[i][j][k]

x = 1
ans = inf
while Ma * x <= a_sum and Mb * x <= b_sum:
    ans = min(ans, dp[-1][Ma * x][Mb * x])
    x += 1

if ans == inf:
    print(-1)
else:
    print(ans)
