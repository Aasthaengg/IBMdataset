n, m = map(int, input().split())
a = list(map(int, input().split()))

match = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
d = dict()
for e in a:
    d[e] = match[e]

dp = [-1] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    for k, v in d.items():
        if i - v >= 0 and dp[i-v] != -1:
            dp[i] = max(dp[i], dp[i-v] * 10 + k)

print(dp[n])
