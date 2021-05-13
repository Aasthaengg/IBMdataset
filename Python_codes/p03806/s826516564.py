import sys
input = sys.stdin.readline

n, ma, mb = map(int,input().split())
A = [0]*n
B = [0]*n
C = [0]*n
for i in range(n) :
    A[i], B[i], C[i] = map(int,input().split())

INF = 10**9

# dp[i][ca][cb] := i番目までの(ca, cb)の最小費用
dp = [[[INF]*401 for j in range(401)] for i in range(n+1)]

dp[0][0][0] = 0
for i in range(1, n+1) :
    dp[i][A[i-1]][B[i-1]] = C[i-1]

for i in range(1, n+1) :
    for ca in range(1, 401) :
        for cb in range(1, 401) :
            if not (ca-A[i-1] >= 0 and cb-B[i-1] >= 0) :
                dp[i][ca][cb] = min(dp[i][ca][cb], dp[i-1][ca][cb])
            else :
                dp[i][ca][cb] = min(dp[i][ca][cb], dp[i-1][ca][cb], dp[i-1][ca-A[i-1]][cb-B[i-1]]+C[i-1])

ans = INF

for ca in range(1, 401) :
    for cb in range(1, 401) :
        if mb*ca == ma*cb :
            ans = min(ans, dp[n][ca][cb])

if ans == INF :
    ans = -1

print(ans)
