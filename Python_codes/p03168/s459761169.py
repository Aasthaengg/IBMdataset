N = int(input())

p = list(map(float,input().split()))

DP = [[0]*(N+1) for i in range(N+1)]

DP[0][0] = 1

for i in range(N):
    for j in range(N+1):
        if j>0:
            DP[i+1][j] = DP[i][j]*(1-p[i]) + DP[i][j-1]*p[i]
        else:
            DP[i+1][j] = DP[i][j]*(1-p[i])

ans = 0

for i in range(N+1):
    if N-i<i:
        ans += DP[N][i]

print(ans)