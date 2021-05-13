import sys
s = input()[::-1]
mod = 10**9 + 7
dp = [0 for i in range(13)]

if s[0] == '?':
    for i in range(10):
        dp[i] += 1
else:
    dp[int(s[0])] += 1

if len(s) == 1:
    print(dp[5])
    sys.exit()

for i, x in enumerate(s[1:], start=1):
    nextdp = [0 for j in range(13)]
    if x != '?':
        a = int(x) * pow(10, i, 13)
        for k in range(13):
            nextdp[(k + a)%13] += dp[k]%mod
            nextdp[(k + a)%13] %= mod
    else:
        for y in range(10):
            a = y * pow(10, i, 13)
            for k in range(13):
                nextdp[(k + a)%13] += dp[k]%mod
                nextdp[(k + a)%13] %= mod
    dp = nextdp
print(dp[5])