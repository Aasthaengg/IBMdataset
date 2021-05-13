import itertools
n = int(input())
p = list(map(float,input().split()))
p = [0] + p
#３回コインを投げて表が２回出る確率＝既に表が２回出ていて３回目に裏が出る確率＋既に表が１回出ていて３回目に表が出る確率
dp = [[0] * (n+1) for i in range(n+1)]
dp[1][0] = 1 - p[1]
dp[1][1] = p[1]
for i in range(1,n):
    for j in range(i+2):
        if j != 0:
            dp[i+1][j] = dp[i][j] * (1 - p[i+1]) + dp[i][j-1] * p[i+1]
        else:
            dp[i+1][j] = dp[i][j] * (1 - p[i+1])
ans = 0

for i in range(n // 2 + 1, n+1):
    ans +=dp[-1][i]
print(ans)