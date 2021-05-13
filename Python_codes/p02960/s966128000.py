import sys

mod = 10**9 + 7
S = sys.stdin.readline().strip()

S = S[::-1]
ls = len(S)
dp = [0] * 13
dp[0] = 1
for i in range(ls):
    ndp = [0] * 13
    # print("S", S[i])
    for j in range(13):
        if dp[j] == 0:
            continue
        digit = pow(10, i, 13)
        if S[i] == "?":
            for k in range(10):
                r = k * digit + j
                r %= 13
                ndp[r] += dp[j]
                ndp[r] %= mod

        else:
            n = int(S[i])
            r = n * digit + j
            r %= 13
            ndp[r] += dp[j]
            ndp[r] %= mod

    # print(ndp)
    dp = ndp

print(dp[5])