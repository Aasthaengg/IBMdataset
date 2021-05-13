mod = 10 ** 9 + 7
inf = float("inf")

s = list(input())
n = len(s)

dp = [[0 for _ in range(13)] for _ in range(n+1)]
dp[0][0] = 1

for i in range(n):
    c = inf
    if s[i] == "?":
        c = -1
    else:
        c = ord(s[i]) - ord('0')
    for j in range(10):
        if c != -1 and c != j:
            continue
        for k in range(13):
            dp[i + 1][(k * 10 + j) % 13] += dp[i][k]
    for j in range(13):
        dp[i + 1][j] %= mod
        
print(dp[n][5])