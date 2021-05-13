N, K = map(int, input().split())
MOD = 10**9+7
C = [[0]*(N+1) for _ in range(N+1)]
C[0][0] = 1

for i in range(1, N+1):
    C[i][0] = 1
    C[i][i] = 1
    
    for j in range(1, i):
        C[i][j] = (C[i-1][j-1]+C[i-1][j])%MOD

for i in range(1, K+1):
    print(C[N-K+1][i]*C[K-1][K-i]%MOD)