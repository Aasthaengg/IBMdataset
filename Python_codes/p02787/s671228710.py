h, n = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
dp = [0] + [10000000000] * h
ret = 10000000000
for i in range(h):
    for j in range(n):
        a, b = ab[j]
        if i + a >= h:
            ret = min(ret, dp[i] + b)
        else:
            dp[i + a] = min(dp[i + a], dp[i] + b)
print(ret)
