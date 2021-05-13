import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
a = [(item, i) for i,item in enumerate(a)]
s = sorted(a)[::-1] # (value, index)
dp = [[None] * (n+1) for _ in range(n+1)] # 高い方からx+y人について、a_i * (p_i - i) + a_i * (i - p_i) の和の最大値

dp[0][0] = 0
tmp = 0
# dp[x][y] : 右にx個、左にy個
for i in range(n):
    val, ind = s[i]
    dp[i+1][0] = dp[i][0] + val * ((n-i-1) - ind)
for i in range(n):
    val, ind = s[i]
    dp[0][i+1] = dp[0][i] + val * (ind - i)

for i in range(2,n+1):
    for x in range(1,i):
        y = i - x
        val, ind = s[i-1]
        v1 = dp[x-1][y] + val * ((n-1 - (x-1)) - ind)
        v2 = dp[x][y-1] + val * (ind - (y-1))
        dp[x][y] = max(v1, v2)
print(max((dp[x][n-x] for x in range(n+1))))