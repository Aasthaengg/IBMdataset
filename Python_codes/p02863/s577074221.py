N,T = map(int,input().split())
A = [[0,0] for _ in range(N+1)]
for i in range(1,N+1):
    a,b = map(int,input().split())
    A[i][0] = a
    A[i][1] = b

A.sort()

dp = [[0 for _ in range(T+1)] for _ in range(N+1)]
for i in range(1,N+1):
    for j in range(T,0,-1):
        if j < T:
            if j < A[i][0]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-A[i][0]]+A[i][1])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + A[i][1])
print (dp[N][T])
