n , m = map(int , input().split())
dp = []
for i in range(n + 1):
    dp.append([])
    for j in range(m + 1):
        dp[i].append(0)
arr = []
for i in range(n):
    arr.append(input())
dp[1][1] = 1
for i in range(1,n + 1):
    for j in range(1,m + 1):
        if arr[i - 1][j - 1] == '#' or (i == 1 and j == 1):
            continue
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
print(dp[n][m] % 1000000007)