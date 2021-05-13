N, = map(int, input().split())
Ps = map(float, input().split())
dp = [0]*((N+1)**2)
dp[0] = 1
for i, p in enumerate(Ps):
    for j in range(N+1):
        dp[(i+1)*(N+1)+j] = p*dp[i*(N+1)+j-1] + (1-p)*dp[i*(N+1)+j]
r = 0
for i in range(N, N//2, -1):
    r += dp[N*(N+1)+i]
print(r)
