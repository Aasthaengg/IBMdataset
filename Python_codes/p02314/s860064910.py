import sys
input = sys.stdin.readline

n, m = map(int,input().split())
c = [0] + list(map(int,input().split()))

dp = [[0] + [n+1 for _ in range(n)] for _ in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if j >=c[i]:
            dp[i][j] = min(dp[i-1][j],dp[i][j-c[i]]+1)
        else:
            dp[i][j] = dp[i-1][j]

print (dp[m][n])
