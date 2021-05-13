n = int(input())
INF = float('inf')
L = [1]
for x in (6, 9):
    i = 1
    while x ** (i + 1) < 10 ** 6:
        L.append(x ** i)
        i += 1
L.sort(reverse=True)
dp = [INF] * (n + 1)
dp[0] = 0
for m in L:
    for i in range(n+1):
        if dp[i] != INF:
            if i + m <= n:
                dp[i+m] = min(dp[i] + 1, dp[i+m])
print(dp[-1])
