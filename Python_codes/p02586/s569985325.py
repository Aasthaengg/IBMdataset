import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
v = [[0 for j in range(c)] for i in range(r)]

dp = [[[0 for j in range(c)] for i in range(r)] for k in range(4)]

for i in range(k):
    ri, ci, vi = map(int, input().split())
    v[ri-1][ci-1] = vi


for i in range(r):
    if i > 0:
        for j in range(c):
            for k in range(4):
                dp[0][i][j] = max(dp[0][i][j], dp[k][i-1][j])
    for j in range(c):
        if j > 0:
            for k in range(4):
                dp[k][i][j] = max(dp[k][i][j], dp[k][i][j-1])
        if v[i][j]:
            for k in reversed(range(1, 4)):
                dp[k][i][j] = max(dp[k][i][j], dp[k-1][i][j]+v[i][j])
        

ans = 0

for k in range(4):
    ans = max(ans, dp[k][r-1][c-1])

print(ans)
        
