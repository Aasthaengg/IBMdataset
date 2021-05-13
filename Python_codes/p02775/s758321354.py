n = input()
lenn = len(n)

dp = [0, 10000]
for d in reversed(n):
    d = int(d)
    dp = [min(d + dp[0], d + 1 + dp[1]), min(10 - d + dp[0], 9 - d + dp[1])]

print(min(dp[0], 1 + dp[1]))