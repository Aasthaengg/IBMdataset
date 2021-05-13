a, b, c, d, e, f = map(int, input().split())
a, b = 100*a, 100*b

dp = [[0, 0] for _ in range(f+1)]
dp[a][0] = a
if b <= f:
    dp[b][0] = b
memo = {(a, 0):0}
for i in range(1, f):
    w, s = dp[i]
    if w:
        for ab in (a, b):
            if i+ab <= f:
                dp[i+ab][0] = w + ab
                dp[i+ab][1] = s
        for cd in (c, d):
            if i+cd <= f and s + cd <= w * e // 100:
                x = dp[i+cd][0] = w
                y = dp[i+cd][1] = s + cd
                memo[(x+y, y)] = y/(x+y)
_, z, y = max([(val, z, y) for (z, y), val in memo.items()])
print(z, y)