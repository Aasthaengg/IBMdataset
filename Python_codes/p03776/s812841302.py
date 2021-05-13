import sys
import math
input = sys.stdin.readline


def comb(n):
    dp = [[0] * (n + 1) for i in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
        dp[i][i] = 1
    for i in range(2, n + 1):
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp


n, a, b = map(int, input().split())
v = list(map(int, input().split()))

v.sort(reverse=True)
comb_list = comb(n)

ans = 0.0
for i in range(a):
    ans += v[i]
ans /= a

x, y = 0, 0
for i in range(n):
    if v[i] == v[a-1]:
        x += 1
        if i < a:
            y += 1

cnt = 0
if y == a:
    for i in range(a, b+1):
        cnt += comb_list[x][i]
else:
    cnt += comb_list[x][y]

print(ans)
print(cnt)

