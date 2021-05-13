
N = int(input())

dp = [[0] * 10 for _ in range(10)]
for n in range(1, N + 1):
    # last
    i = n % 10

    # first
    while n >= 10:
        n //= 10
    j = n % 10

    dp[i][j] += 1

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        ans += dp[i][j] * dp[j][i]

print(ans)
