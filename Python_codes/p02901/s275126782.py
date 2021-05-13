INF = 10**18

N, M = map(int,input().split())

A = []
B = []
C = []

for _ in range(M):
    a, b = map(int,input().split())
    A.append(a)
    B.append(b)
    c = tuple(map(int,input().split()))
    C.append(c)
    
dp = [[INF for j in range(2**N)] for i in range(M + 1)]
dp[0][0] = 0

for i in range(M):
    s = 0
    for k in range(B[i]):
        s += 2**(C[i][k] - 1)
    for j in range(2**N):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        dp[i + 1][j | s] = min(dp[i + 1][j | s], dp[i][j] + A[i])
        
res = dp[M][2**N - 1]

print(res if res != INF else -1)