N, K = map(int, input().split())
mod = 998244353
lr = []
for k in range(K):
    lr.append(list(map(int, input().split())))
dp = [0]*(2*N+1)
dp[0] = 1
dpsum = 0
for i in range(N):
    dpsum += dp[i]%mod
    for k in lr:
        l = k[0]
        r = k[1]

        dp[i+l] += dpsum%mod
        dp[i+r+1] -= dpsum%mod
        
print(dp[N-1]%mod)