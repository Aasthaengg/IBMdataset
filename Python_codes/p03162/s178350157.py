n = int(input())
X = [0]*n
for i in range(n):
    t = list(map(int, input().split()))
    X[i] = t


dp = [[0, 0, 0] for _ in range(n)]
dp[0] = X[0]


for i in range(1, n):
    dp[i][0] = max(dp[i-1][1]+X[i][0], dp[i-1][2]+X[i][0])
    dp[i][1] = max(dp[i-1][0]+X[i][1], dp[i-1][2]+X[i][1])
    dp[i][2] = max(dp[i-1][0]+X[i][2], dp[i-1][1]+X[i][2])

print(max(dp[-1]))
