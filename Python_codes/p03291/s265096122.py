s = input()
mod = 1000000007
dp = [1, 0, 0, 0]
for c in s:
    newdp = [n for n in dp]
    if c == 'A':
        newdp[1] = (newdp[1] + dp[0]) % mod
    if c == 'B':
        newdp[2] = (newdp[2] + dp[1]) % mod
    if c == 'C':
        newdp[3] = (newdp[3] + dp[2]) % mod
    if c == '?':
        newdp[0] = (newdp[0] * 3) % mod
        newdp[1] = (newdp[1] * 3 + dp[0]) % mod
        newdp[2] = (newdp[2] * 3 + dp[1]) % mod
        newdp[3] = (newdp[3] * 3 + dp[2]) % mod
    dp = newdp
print(dp[3])
