s = input()[::-1]

dp = [0] * 13
dp[0] = 1
mod = 10 ** 9 + 7

for i, char in enumerate(s):
    dp_new = [0] * 13

    if char != '?':
        l = [int(char)]
    else:
        l = list(range(10))

    for k in l:
        tmp = pow(10, i, 13)
        tmp = (k * tmp) % 13

        for j in range(13):
            dp_new[(j + tmp) % 13] += dp[j]

    dp = []
    for x in dp_new:
        dp.append(x % mod)

print(dp[5])
