l = input()
p = 10 ** 9 + 7
dp = [0, 1]
for i in l:
    dp2 = [j % p for j in dp]
    if i == "0":
        dp[0] = dp2[0] * 3
        dp[1] = dp2[1]
    else:
        dp[0] = dp2[0] * 3 + dp2[1]
        dp[1] = dp2[1] * 2
print(sum(dp) % p)
