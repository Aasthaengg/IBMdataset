N,M,Q = map(int,input().split())
A = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    l,r = map(int,input().split())
    A[l][r] += 1
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp[N][1] = A[N][1]
for j in range(2,N+1):
    dp[N][j] = dp[N][j-1]+A[N][j]
for i in range(N-1,0,-1):
    dp[i][1] = dp[i+1][1]+A[i][1]
for i in range(N-1,0,-1):
    for j in range(2,N+1):
        dp[i][j] = A[i][j]+dp[i][j-1]+dp[i+1][j]-dp[i+1][j-1]
for _ in range(Q):
    p,q = map(int,input().split())
    print(dp[p][q])