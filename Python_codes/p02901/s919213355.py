n,m = map(int,input().split())
ab = []
c = []
for i in range(m):
    ab.append(list(map(int,input().split())))
    s = 0
    for j in map(int,input().split()):
        s += 2**(j-1)
        
    c.append(s)

dp = [[float("INF")]*(2**n) for i in range(m+1)]

dp[0][0] = 0

for i in range(m):
    for j in range(2**n):
        if dp[i][j] != float("INF"):
            dp[i+1][j] = min(dp[i+1][j],dp[i][j])
            x = j|c[i]
            dp[i+1][x] = min(dp[i+1][x],dp[i][j]+ab[i][0])

if dp[-1][-1] == float("INF"):
    print(-1)
else:
    print(dp[-1][-1])

