def inpl(): return list(map(int, input().split()))
MOD = 10**9 + 7
N, M = inpl()
S = [0] + inpl()
T = [0] + inpl()

DP = [[1]*(N+1) for _ in range(M+1)]

for i in range(1, M+1):
    for j in range(1, N+1):
        if S[j] == T[i]:
            DP[i][j] = (DP[i][j-1] + DP[i-1][j])%MOD
        else:
            DP[i][j] = (DP[i][j-1] + DP[i-1][j] - DP[i-1][j-1])%MOD
print(DP[-1][-1])