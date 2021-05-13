S = ''.join(list(reversed(input())))
N = len(S)
p = 13
mod = 10**9 + 7

dp = [[0]*p for _ in range(N)]

if S[0] == '?':
    for j in range(10):
        dp[0][j] = 1
else:
    dp[0][int(S[0])] = 1

b = 10
for i in range(N - 1):
    r = []
    if S[i + 1] == '?':
        for j in range(10):
            r.append(b * j % p)
    else:
        r.append(b * int(S[i + 1]) % p)

    for j in range(len(r)):
        for k in range(p):
            if dp[i][k] > 0:
                dp[i + 1][(k + r[j]) % p] += dp[i][k]
                dp[i + 1][(k + r[j]) % p] %= mod

    b *= 10
    b %= p

print(dp[N - 1][5] % mod)