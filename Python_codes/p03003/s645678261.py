N,M = map(int,input().split())
MOD = 10**9+7
S = list(map(int,input().split()))
T = list(map(int,input().split()))
DP = [[1]*(M+1) for i in range(N+1)]
for i in range(N):
    hoge = 0
    for j in range(M):
        if S[i] == T[j]:
            hoge += DP[i][j]
            hoge %= MOD
        DP[i+1][j+1] = (DP[i][j+1] + hoge)%MOD
print(DP[-1][-1])
