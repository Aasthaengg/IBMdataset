H,N = map(int,input().split())
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)
inf = 10**10
f = H+max(A)+1
dp = [[inf]*f for _ in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
    dp[i][0] = 0
    for j in range(f):
        dp[i][j] = dp[i-1][j]
        if j-A[i-1]>=0:
            dp[i][j] = min(dp[i][j],dp[i][j-A[i-1]]+B[i-1])
print(min(dp[-1][H:]))