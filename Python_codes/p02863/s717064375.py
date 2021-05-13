import sys
input = sys.stdin.readline

n, t = [int(x) for x in input().split()]
ab = []
for _ in range(n):
    ab.append([int(x) for x in input().split()])
ab_rev = ab[::-1]

dp1 = [[0] * t for _ in range(n + 1)] # 前から見た
dp2 = [[0] * t for _ in range(n + 1)] # 後ろから見た

for i in range(1, n + 1):
    a, b = ab[i - 1]
    for j in range(t):
        if j - a >= 0:
            dp1[i][j] = max(dp1[i - 1][j - a] + b, dp1[i - 1][j])
        else:
            dp1[i][j] = dp1[i - 1][j]

for i in range(1, n + 1):
    a, b = ab_rev[i - 1]
    for j in range(t):
        if j - a >= 0:
            dp2[i][j] = max(dp2[i - 1][j - a] + b, dp2[i - 1][j])
        else:
            dp2[i][j] = dp2[i - 1][j]

ans = -1

for i in range(1, n + 1):
    for j in range(t):
        ans = max(ans, dp1[i - 1][j] + dp2[n - i][t - 1 - j] + ab[i - 1][1])

print(ans)