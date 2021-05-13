n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int , input().split())))
dp = [[0 for j in range(3)] for i in range(n + 2)]
for i in range(1 , n + 1):
    dp[i][0] = arr[i - 1][0] + max(dp[i - 1][1] , dp[i - 1][2])
    dp[i][1] = arr[i - 1][1] + max(dp[i - 1][0] , dp[i - 1][2])
    dp[i][2] = arr[i - 1][2] + max(dp[i - 1][0] , dp[i - 1][1])
print(max(dp[n]))