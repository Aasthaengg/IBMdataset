n = int(input())
dp = [[0] * 3 for i in range(n + 1)]
a, b, c = [], [], []
for i in range(n):
    a_, b_, c_ = map(int, input().split())
    a.append(a_)
    b.append(b_)
    c.append(c_)
for i in range(1, n + 1):
    dp[i][0] = max(dp[i - 1][1] + a[i - 1], dp[i - 1][2] + a[i - 1])
    dp[i][1] = max(dp[i - 1][0] + b[i - 1], dp[i - 1][2] + b[i - 1])
    dp[i][2] = max(dp[i - 1][0] + c[i - 1], dp[i - 1][1] + c[i - 1])
print(max(dp[n][0], dp[n][1], dp[n][2]))