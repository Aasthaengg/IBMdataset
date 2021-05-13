N = int(input())

happy = [list(map(int,input().split())) for i in range(N)]

dp = []
for i in range(N+1):
    dp.append([])
    for j in range(3):
        dp[i].append(0)

for i in range(N):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i+1][k] = max(dp[i+1][k], dp[i][j] + happy[i][k])

res = 0
for i in range(3):
    res = max(res, dp[N][i])

print(res)

#print(happy)