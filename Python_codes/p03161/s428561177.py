a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
n = a[0]
k = a[1]
dp = [0] + [float("inf")]*(n - 1)
for x in range(n):
    y = x + 1
    while y - x <= k:
        if y < n:
            dp[y] = min(dp[y], dp[x] + abs(b[x] - b[y]))
        y += 1
print(dp[-1])