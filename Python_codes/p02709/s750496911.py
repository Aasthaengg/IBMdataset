n = int(input())
a = list(map(int, input().split()))
dp = [[0] * (n+1) for i in range(n+1)]
A = []
for i in range(n):
    A.append([a[i], i])
A.sort(reverse=True)
for i in range(1, n+1):
    for j in range(i+1):
        if j == 0:
            dp[j][i-j] = dp[j][i-j-1] + A[i-1][0] * abs(n-i-A[i-1][1])
        elif j == i:
            dp[j][i-j] = dp[j-1][i-j] + A[i-1][0] * abs(A[i-1][1]-i+1)
        else:
            dp[j][i-j] = max(dp[j][i-j-1] + A[i-1][0] * abs(n-i+j-A[i-1][1]), dp[j-1][i-j] + A[i-1][0] * abs(A[i-1][1]-j+1))
ans = 0
for i in range(n+1):
    ans = max(ans, dp[i][n-i])
print(ans)