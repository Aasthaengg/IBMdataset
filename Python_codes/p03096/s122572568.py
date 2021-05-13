MOD = 10**9+7
n = int(input())
c = [int(input())]
for _ in range(n-1):
    x = int(input())
    if x != c[-1]: c.append(x)
n = len(c)
t = [-1] * (10**5*2+1)
t[c[0]] = 0
dp = [1] + [0] * (n-1)

for i in range(1, n):
    dp[i] += dp[i-1]
    if t[c[i]] != -1:
        dp[i] += dp[t[c[i]]]
    dp[i] %= MOD
    t[c[i]] = i

print(dp[-1])
