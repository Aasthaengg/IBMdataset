s = input()
n = len(s)


MOD = 2019
dp = [0] * MOD
dp[0] += 1

rem = 0
base = 1
for i in range(n):
    d = int(s[n-i-1])
    rem = (rem + base * d) % MOD
    # print((i, d, rem))
    dp[rem] += 1
    base *= 10
    base %= MOD

ans = 0
for i in range(MOD):
    ans += (dp[i]*(dp[i]-1)) // 2
print(ans)
