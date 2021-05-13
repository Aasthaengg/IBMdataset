n, m = map(int, input().split())
c = list(map(int, input().split()))

DP = [[100000 for _ in range(n+1)] for _ in range(m+1)]
DP[0][0] = 0

for i in range(m):
    for j in range(n+1):
        if(j >= c[i]):
            DP[i+1][j] = min(DP[i][j], DP[i+1][j-c[i]]+1)
        else:
            DP[i+1][j] = DP[i][j]

print(DP[m][n])
