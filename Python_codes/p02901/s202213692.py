INF = float("INF")
n,m = map(int,input().split())
A = [0]*m
C = [0]*m
for i in range(m):
    a,b = map(int,input().split())
    A[i] = a
    for j in map(int,input().split()):
        j -= 1
        C[i] += 1<<j 

dp = [[INF]*(m+1) for _ in range(1<<n)]
dp[0][0] = 0
for i in range(1<<n):
    for j in range(m):
        dp[i][j+1] = min(dp[i][j],dp[C[j]&i^i][j] + A[j])

# for i in range(1<<n): print(dp[i])
print(dp[-1][-1] if dp[-1][-1] != INF else -1)