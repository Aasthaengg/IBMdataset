a, b, c, d, e, f = map(int, input().split())
a, b = 100*a, 100*b
 
dp = [[0, 0] for _ in range(f+1)]
memo = {(a, 0):0}
dp[a][0] = a
if b <= f:
    dp[b][0] = b
for i in range(1, f):
    if dp[i][0]:
        if i+a <= f:
            dp[i+a][0] = dp[i][0] + a
            dp[i+a][1] = dp[i][1]
        if i+b <= f:
            dp[i+b][0] = dp[i][0] + b
            dp[i+b][1] = dp[i][1]
        if i+c <= f and dp[i][1] + c <= dp[i][0] * e // 100:
            x = dp[i+c][0] = dp[i][0]
            y = dp[i+c][1] = dp[i][1] + c
            memo[(x+y, y)] = y/(x+y)
        if i+d <= f and dp[i][1] + d <= dp[i][0] * e // 100:
            x = dp[i+d][0] = dp[i][0]
            y = dp[i+d][1] = dp[i][1] + d
            memo[(x+y, y)] = y/(x+y)
_, z, y = max([(val, z, y) for (z, y), val in memo.items()])
print(z, y)