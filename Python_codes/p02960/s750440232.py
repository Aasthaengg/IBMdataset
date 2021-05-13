mod = 10 ** 9 + 7

S = input()

l = len(S)
dp = [[0 for i in range(13)] for j in range(l+1)]

dp[0][0] = 1

for i, num in enumerate(S):

    if num == "?":
        for k in range(10):
            for j in range(13):
                dp[i+1][((j * 10) + k) % 13] += dp[i][j]
                # nextdp[((j * 10) + k) % 13] %= mod

    else:
        k = int(num)
        for j in range(13):
            dp[i+1][((j * 10) + k) % 13] += dp[i][j]
            # nextdp[((j * 10) + k) % 13] %= mod

    for j in range(13):
        dp[i+1][j] %= mod

print(dp[l][5])
