mod = 10 ** 9 + 7

S = input()

dp = [0] * 13

dp[0] = 1

l = len(S)

for i in S:
    nextdp = [0] * 13
    if i == "?":
        for k in range(10):
            for j in range(13):
                nextdp[((j * 10) + k) % 13] += dp[j]
                # nextdp[((j * 10) + k) % 13] %= mod

    else:
        k = int(i)
        for j in range(13):
            nextdp[((j * 10) + k) % 13] += dp[j]
            # nextdp[((j * 10) + k) % 13] %= mod

    dp = [nextdp[i] % mod for i in range(13)]

    # for i in range(13):
    #     dp[i] = nextdp[i] % mod

print(dp[5])
