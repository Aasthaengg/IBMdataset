N,M = list(map(int,input().split()))
S = list(map(int,input().split()))
S = [0] + S
T = list(map(int,input().split()))
T = [0] + T
dp = [[0] * (N+1)  for _ in range(M+1)]
DP = [[0] * (N+1)  for _ in range(M+1)]
dp[0][0] = 1
for n in range(N+1):
    DP[0][n] = 1
for m in range(M+1):
    DP[m][0] = 1
# s = 0
# for i in range(N+1):
#     for j in range(M+1):
#         if S[i] == T[j]:
#             for i2 in range(i):
#                 for j2 in range(j):
#                     dp[i][j] += dp[i2][j2]
#             s += dp[i][j]
# print(s)
for n in range(1,N+1):
    for m in range(1,M+1):
        if S[n] == T[m]:
            dp[m][n] = DP[m-1][n-1]
        DP[m][n] = (DP[m-1][n] + DP[m][n-1] + dp[m][n] - DP[m-1][n-1]) % (10**9+7)
print(DP[M][N])