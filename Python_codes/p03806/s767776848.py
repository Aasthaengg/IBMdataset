N, Ma, Mb = map(int, input().split())
A = []
B = []
C = []
for _ in range(N):
    a, b, c = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)

INF = 4001
Na = sum(A)
Nb = sum(B)
dp = [[[INF]*(Nb+1) for _ in range(Na+1)] for _ in range(N+1)]
dp[0][0][0] = 0

for i in range(N):
    for j in range(Na+1):
        for k in range(Nb+1):
            if j < A[i] or k < B[i]:
                dp[i+1][j][k] = dp[i][j][k]
            else:
                dp[i+1][j][k] = min(dp[i][j][k], dp[i][j-A[i]][k-B[i]]+C[i])
            
ans = INF
for i in range(1, N+1):
    for j in range(1, Na+1):
        for k in range(1, Nb+1):
            if j*Mb == k*Ma:
                ans = min(ans, dp[i][j][k])
                
if ans == INF:
    ans = -1
    
print(ans)