# n<3000, t<3000, a,b <3000
import sys

input = sys.stdin.buffer.readline

n, t = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(n)]
rAB = AB[::-1]
dp1 = [[0] * (t + 1) for _ in range(n + 1)]
dp2 = [[0] * (t + 1) for _ in range(n + 1)]

for i in range(n):
    ni = i + 1
    a, b = AB[i]
    for j in range(t + 1):
        nj = j + a
        if nj <= t:
            dp1[ni][nj] = max(dp1[i][j] + b, dp1[ni][nj])
        dp1[ni][j] = max(dp1[ni][j], dp1[i][j])
    c, d = rAB[i]
    for j in range(t + 1):
        nj = j + c
        if nj <= t:
            dp2[ni][nj] = max(dp2[i][j] + d, dp2[ni][nj])
        dp2[ni][j] = max(dp2[ni][j], dp2[i][j])

ans = 0
# i-1まで→先頭i個
# 後ろはn-(i+1)個
for i in range(n):
    for j in range(t):
        temp = AB[i][1]
        if i >= 1:
            temp += dp1[i][j]
        if n - i - 1 >= 1:
            temp += dp2[n - i - 1][t - 1 - j]
        ans = max(ans, temp)
print(ans)
