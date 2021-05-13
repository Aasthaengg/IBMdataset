n, m = map(int, input().split())

a = []
for i in range(m):
    a.append(int(input()))
a = set(a)

dp = [0] * (n + 1)
dp[0] = 1
for now in range(0, n + 1):
    for next_step in range(now + 1, min(n + 1, now + 3)):
        if not next_step in a:
            dp[next_step] += dp[now]
            dp[next_step] %= 1000000007

print(dp[n])