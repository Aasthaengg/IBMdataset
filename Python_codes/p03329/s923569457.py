n = int(input())
list_c = [9 ** i for i in range(6)]
list_c += [6 ** i for i in range(1, 7)]
list_c.sort()

dp = [float('inf')] * (n + 1)
dp[0] = 0
for i in range(n):
    for c in list_c:
        if i + c <= n:
            dp[i + c] = min(dp[i + c], dp[i] + 1)

print(dp[-1])