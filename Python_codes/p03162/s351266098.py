def maxPoints(a,b,c,N):
    dp = [[0]*3 for _ in range(N)]
    dp[0][0] = a[0]
    dp[0][1] = b[0]
    dp[0][2] = c[0]

    for i in range(1,N):
        dp[i][0] = a[i] + max(dp[i-1][1],dp[i-1][2])
        dp[i][1] = b[i] + max(dp[i-1][0],dp[i-1][2])
        dp[i][2] = c[i] + max(dp[i-1][1],dp[i-1][0])
    
    return max(dp[N-1])

n = int(input())
a = [0] * n
b = a.copy()
c = a.copy()
for i in range(n):
    a[i],b[i],c[i] = map(int,input().split())
print(maxPoints(a,b,c,n))