s = list(input())
MOD = 10**9 + 7
cnt = [[] for _ in range(len(s))]
i = len(s) - 1
de = 1

while i >= 0:
    if s[i] == '?':
        for j in range(10):
            cnt[i].append((j * de) % 13)
    else: cnt[i].append((int(s[i]) * de) % 13)
    i -= 1
    de *= 10
    de %= 13

dp = [[0]*13 for _ in range(len(s))]
for i in cnt[0]:
    dp[0][i] = 1
for i in range(1, len(s)):
    for j in cnt[i]:
        for k in range(13):
            if dp[i-1][k] != 0:
                dp[i][(j + k)%13] += dp[i - 1][k]
                dp[i][(j + k)%13] %= MOD
print(dp[-1][5])
