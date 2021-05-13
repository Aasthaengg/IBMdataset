import sys
input = sys.stdin.readline

inf = float('inf')

N,Ma,Mb = map(int,input().split())

# dp[i][j][k]: i番目までみてj(g), k(g)となるような最小予算
dp = [[[inf]*401 for _ in range(401)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    a,b,c = map(int,input().split())
    for j in range(401):
        for k in range(401):
            dp[i+1][j][k] = dp[i][j][k]
            if j - a >= 0 and k - b >= 0 and dp[i+1][j][k] > dp[i][j-a][k-b] + c:
                dp[i+1][j][k] = dp[i][j-a][k-b] + c

ans = inf

for j in range(1,401):
    for k in range(1,401):
        if j * Mb == Ma * k and ans > dp[N][j][k]:
            ans = dp[N][j][k]

if ans == inf:
    ans = -1
print(ans)