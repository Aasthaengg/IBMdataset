dp = [0, 2]
for d in map(int, reversed(input())):
    dp = [min(d + dp[0], d + 1 + dp[1]), min(10 - d + dp[0], 9 - d + dp[1])]

print(min(dp[0], 1 + dp[1]))
