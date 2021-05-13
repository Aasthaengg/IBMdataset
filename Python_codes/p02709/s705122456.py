n = int(input())
a = list(map(int,input().split()))

ans = 0
dp = [[0] * (n+1) for _ in range(n+1)]

li = []
for i in range(n):
    li.append((a[i],i))

li.sort(reverse = True)

for i in range(1,n+1):
    tmp = li[i-1]
    for ii in range(i+1):
        jj = i - ii
        if ii == 0:
            dp[ii][jj] = dp[ii][jj-1] + tmp[0] * abs((n - jj) - tmp[1])
        elif jj == 0:
            dp[ii][jj] = dp[ii-1][jj] + tmp[0] * abs((ii - 1) - tmp[1])
        else:
            dp[ii][jj] = max(dp[ii][jj-1] + tmp[0] * abs((n - jj) - tmp[1]), dp[ii-1][jj] + tmp[0] * abs((ii - 1)- tmp[1]))


for i in range(n+1):
    ans = max(ans, dp[i][n-i])

print(ans)
