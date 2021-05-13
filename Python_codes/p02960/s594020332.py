MOD = 10 ** 9 + 7
pow_10_i_13 = [pow(10, i, 13) for i in range(6)]

s = input()

dp = [0] * 13
dp[0] = 1
for i, c in enumerate(reversed(s)):
    if c == '?':
        tmp = [0] * 13
        for j in range(10):
            shift = j * pow_10_i_13[i % 6] % 13
            for k in range(13):
                tmp[k] += dp[k-shift]
                tmp[k] %= MOD
        dp = tmp
    else:
        shift = int(c) * pow_10_i_13[i % 6] % 13
        dp = dp[-shift:] + dp[:-shift]

print(dp[5])
