n, m = list(map(int, input().split()))
a = []
for _ in range(m):
    a.append(int(input()))
a = set(a)
cur = 0
dp = [0 for _ in range(n + 1)]
dp[0], dp[1] = 1, 1
if 1 in a:
    dp[1] = 0
for i in range(2, n + 1):
    if i in a:
        continue
    dp[i] = (dp[i - 1] + dp[i - 2]) % (10 ** 9 + 7)
print(dp[n])
