S = input()
N = len(S)
MOD = 10**9 + 7
DP = [[1] * 4 for _ in range(N + 1)]
# initialize
DP[N][3] = 1
DP[N][0] = 0
DP[N][1] = 0
DP[N][2] = 0

for i in range(N-1, -1, -1):
    for j in range(3, -1, -1):
        DP[i][j] = DP[i+1][j] * (3 if S[i]=='?' else 1)
        if j<3:
            DP[i][j] += DP[i + 1][j + 1] * (1 if (S[i]=='ABC'[j] or S[i]=='?') else 0)
        DP[i][j] %= MOD

ans = DP[0][0]
print(ans)
            
