n = int(input())

dp = [[0]*3 for i in range(n+1)]
a = []

for i in range(n):
    a.append(list(map(int,input().split())))

for i in range(n):
    for j in range(3):
        for k in range(3):
            if j==k:
                continue
            dp[i+1][j] = max(dp[i+1][j],dp[i][k] + a[i][j])

print(max(dp[n]))
