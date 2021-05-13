N, K = map(int, input().split())
*A, = map(int, input().split())
dp = [[0]*N for _ in range(60)]

for i in range(N):
    dp[0][i] = A[i] - 1

for k in range(1, 60):
    for n in range(N):
        dp[k][n] = dp[k - 1][dp[k - 1][n]]

res = []
for i in range(60):
    if (K>>i)&1:
        res.append(i)
    
pos = 0
for i in res:
    pos = dp[i][pos]
print(pos + 1)