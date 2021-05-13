import sys
input = sys.stdin.buffer.readline

n = int(input())
a = list(map(int,input().split()))

dp = [[0]*(n+1) for _ in range(n+1)]

b = []
for i in range(n):
    b.append(a[i]*n + i)
b.sort(reverse = True)

for i in range(n+1):
    for j in range(n+1-i):
        val,idx = divmod(b[i+j-1],n)
        if i > 0:
            dp[i][j] = max(dp[i][j],dp[i-1][j] + val*abs(idx-i+1))
        if j > 0:
            dp[i][j] = max(dp[i][j],dp[i][j-1] + val*abs(idx-n+j))

ans = 0
for i in range(n+1):
    if ans < dp[i][n-i]:
        ans = dp[i][n-i]
print(ans)