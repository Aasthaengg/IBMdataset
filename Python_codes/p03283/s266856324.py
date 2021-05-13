N,M,Q = map(int,input().split())
A = [[0 for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    L,R = map(int,input().split())
    A[L][R] += 1
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp[N][N] = A[N][N]
for i in range(N-1,0,-1):
    for j in range(i,N+1):
        dp[i][j] = A[i][j]
        if j>i:
            dp[i][j] += dp[i+1][j]+dp[i][j-1]-dp[i+1][j-1]
for _ in range(Q):
    p,q = map(int,input().split())
    print(dp[p][q])