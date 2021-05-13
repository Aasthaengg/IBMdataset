MOD = 10 ** 9 + 7

n, m = map(int, input().split())
a_s = [int(input()) for _ in range(m)] + [n + 1]
dp = [0 for _ in range(n + 1)]
dp[0] = 1
a_pos = 0
for i in range(1, n + 1):
    if a_s[a_pos] == i:
        a_pos += 1
        continue
    dp[i] = dp[i - 1] + dp[i - 2]
    dp[i] %= MOD
print(dp[-1])
