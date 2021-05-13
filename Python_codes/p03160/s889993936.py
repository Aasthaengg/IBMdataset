a = int(input())
b = [int(x) for x in input().split()]
dp = [0] + [None] * (a - 1)
dp[1] = abs(b[0] - b[1])
for x in range(2, a):
    dp[x] = min(dp[x - 2] + abs(b[x] - b[x - 2]), dp[x - 1] + abs(b[x] - b[x - 1]))
print(dp[-1])