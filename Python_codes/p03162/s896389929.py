n = int(input())
li = [-1]*n

for i in range(n):
    li[i] = [int(w) for w in input().split()]

dp = [[-1] * 3 for i in range(n)]
dp[0][0] = li[0][0]
dp[0][1] = li[0][1]
dp[0][2] = li[0][2]


for i in range(1, n):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i][j] = max(dp[i][j], dp[i - 1][k] + li[i][j])

print(max(dp[n - 1]))
