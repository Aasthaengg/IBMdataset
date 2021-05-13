n, m = map(int, input().split())
an = [int(input()) for _ in range(m)]

dp = [0 for _ in range(n+1)]
dp[0] = 1
mod = 10**9 + 7

if m == 0:
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % mod
    print(dp[n])
    exit()

if an[0] == 1:
    dp[1] = 0
    a = 1
    if len(an) == 1:
        a = 0
else:
    dp[1] = 1
    a = 0

for i in range(2, n+1):
    if i == an[a]:
        dp[i] = 0
        a += 1
        if a == len(an):
            a -= 1
    else:
        dp[i] = (dp[i-1] + dp[i-2]) % mod

print(dp[n])
