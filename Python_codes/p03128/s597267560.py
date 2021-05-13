n, m = map(int, input().split())
a = list(map(int, input().split()))
matches = [100, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [""]
for i in range(1, n + 1):
    dp.append(None)
    for d in a:
        m = matches[d]
        if i - m >= 0 and dp[i - m] is not None:
            r = max(dp[i - m] + str(d), str(d) + dp[i - m])
            if dp[i] is None or len(r) > len(dp[i]) or len(r) == len(dp[i]) and r > dp[i]:
                dp[i] = r
print(dp[n])
