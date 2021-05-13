l = input()
mod = 10 ** 9 + 7

ln = len(l)
dp = [[0] * 2 for _ in range(ln + 1)]
dp[0][1] = 1

for i, e in enumerate(l, 1):
    # smaller -> smaller
    if e == "1":
        dp[i][0] += dp[i-1][0] * 3
    else:
        dp[i][0] += dp[i-1][0] * 3
    # exact -> smaller
    if e == "1":
        dp[i][0] += dp[i-1][1]
    # exact -> exact
    if e == "1":
        dp[i][1] += dp[i-1][1] * 2
    else:
        dp[i][1] += dp[i-1][1]

    dp[i][0] %= mod
    dp[i][1] %= mod

ans = dp[ln][0] + dp[ln][1]
ans %= mod
print(ans)
#print(*dp, sep="\n")
