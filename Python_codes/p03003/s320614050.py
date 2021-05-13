n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))

MOD = 10 ** 9 + 7

dp = [[0 for _ in range(m)] for _ in range(n)]
sd = [[0 for _ in range(m)] for _ in range(n)]

ans = 1

if s[0] == t[0]:
    dp[0][0] = 1
    sd[0][0] = 1
    ans += 1

for i in range(1, n):
    if s[i] == t[0]:
        dp[i][0] = 1
        ans += 1
    sd[i][0] = dp[i][0] + sd[i-1][0]

for j in range(1, m):
    if s[0] == t[j]:
        dp[0][j] = 1
        ans += 1
    sd[0][j] = dp[0][j] + sd[0][j-1]

for i in range(1, n):
    for j in range(1, m):
        if s[i] == t[j]:
            dp[i][j] = (sd[i-1][j-1] + 1) % MOD
            ans = (ans + dp[i][j]) % MOD
        sd[i][j] = (sd[i-1][j] + sd[i][j-1] - sd[i-1][j-1] + dp[i][j]) % MOD

print(ans)

