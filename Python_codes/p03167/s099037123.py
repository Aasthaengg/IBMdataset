n, m= list(map(int,input().split()))
arr = []
for i in range(n):
    arr.append(list(input()))
dp = []
dp.append([0]*(m+1))
for i in range(n):
    dp.append([0]+[1]*(m))
dp[1][1] = 1
for i in range(n):
    for g in range(m):
        dp[1][1] = 1
        if arr[i][g] != "#":
            dp[i+1][g+1] = (dp[i][g+1]+dp[i+1][g])%1000000007
        else:
            dp[i+1][g+1] = 0
print(dp[n][m])