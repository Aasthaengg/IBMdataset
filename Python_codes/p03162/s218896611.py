n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

dp = [[0,0,0] for _ in range(n)]

for i in range(n):
    if i == 0:
        for j in range(3):
            dp[i][j] = li[i][j]
    else:
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                dp[i][k] = max(dp[i][k], dp[i-1][j] + li[i][k])

print(max(dp[-1]))