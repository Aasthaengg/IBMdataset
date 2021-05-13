h, n = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

dp = [h * 10 ** 4] * (h + 1)
dp[0] = 0
for i in range(n):
    for j in range(min(a[i], h+1)):
        dp[j] = min(dp[j], b[i])
    for j in range(a[i], h + 1):
        dp[j] = min(dp[j], dp[j - a[i]] + b[i])
print(dp[-1])