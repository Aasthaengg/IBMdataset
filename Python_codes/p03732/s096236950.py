n,W = map(int,input().split())
w = [0]*n
v = [0]*n
for i in range(n): w[i],v[i] = map(int,input().split())
x = w[0]
for i in range(n): w[i] -= x
dp = [[[0]*(4*n+1) for _ in range(n+1)] for _ in range(n+1)]

for i in range(n):
    for j in range(i+1):
        for k in range(4*n+1):
            if (j+1)*x+k <= W and k-w[i] >= 0:
                dp[i+1][j+1][k] = max(dp[i+1][j+1][k],dp[i][j][k-w[i]]+v[i])
            dp[i+1][j][k] = max(dp[i+1][j][k],dp[i][j][k])

"""
for i in range(n+1):
    print(i,"///////////////////////////////////////////////")
    for j in range(n+1):
        print(dp[i][j])
"""
print(max(max(dp[n][j]) for j in range(n+1)))