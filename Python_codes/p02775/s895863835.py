n = input()
dp = [0, 10000]
for d in reversed('0' + n):
    newdp = []
    newdp.append(min(int(d) + dp[0], int(d) + 1 + dp[1]))
    newdp.append(min(10 - int(d) + dp[0], 10 - int(d) - 1 + dp[1]))
    dp = newdp
print(dp[0])
