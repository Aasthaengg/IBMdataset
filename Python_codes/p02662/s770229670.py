
N,S = map(int,input().split())
A = list(map(int,input().split()))
#%%
# b = [[0]*(S+1) for _ in range(N+1)]
# b[0][0] = int(S==0)
MOD = 998244353

# for r in range(N):
#     for s in range(S+1):
#         b[r+1][s] += b[r][s]
#         if s-A[r]>=0:
#             b[r+1][s] += b[r][s-A[r]]
#         if s==A[r] or s==0:
#             b[r+1][s] += 1
#         b[r+1][s] %= MOD

# ans = 0
# for i in range(N):  
#     ans += b[i+1][S]
#     ans %= MOD
    
# print(ans)

dp = [[0]*(S+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(S+1):
        dp[i+1][j] += 2*dp[i][j]
        if j-A[i]>=0:
            dp[i+1][j] += dp[i][j-A[i]]
        dp[i+1][j] %= MOD

print(dp[N][S])