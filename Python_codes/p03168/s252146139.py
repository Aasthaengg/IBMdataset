N = int(input())
P = [float(v) for v in input().split()]
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

#  for i,p in enumerate(P,1): dp[i][0] = (1-p)
dp[0][0] = 1
dp[1][0] = P[0]

threshold = N // 2

ans = 0
for i in range(1,N+1):
    p = P[i-1]
    for j in range(0,N+1):
        if j != 0:
            dp[i][j] = (dp[i-1][j-1] * p) + dp[i-1][j] * (1-p)
        else:
            dp[i][j] = dp[i-1][j] * (1-p)

ans = 0

for i,v in enumerate(dp[N]):
    if i > threshold:
        ans += v
print(ans)
