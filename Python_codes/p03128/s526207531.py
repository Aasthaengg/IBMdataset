n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

dp = [(0, 0)] * (n+1)
ma = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]

for i in range(n):
    if i!=0 and dp[i] == (0, 0):
        continue
    for j in a:
        t = dp[i]
        k = i + ma[j]
        if k <= n:
            dp[k] = max(dp[k], (t[0] + j * 10 ** t[1], t[1] + 1))
            dp[k] = max(dp[k], (t[0]*10 + j, t[1] + 1))

print(dp[-1][0])
