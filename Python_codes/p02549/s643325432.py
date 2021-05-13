N, K = map(int, input().split())
LRs = [list(map(lambda x:int(x), input().split())) for _ in range(K)]

mod = 998244353
#%%
options = []

for LR in LRs:
    for i in range(LR[0], LR[1]+1):
        options.append(i)

options = sorted(options)

dp = [0 for _ in range(N+1)]
dp[1] = 1

rui = [0 for _ in range(N+1)]
rui[1] = 1

for i in range(2,N+1):
    for LR in LRs: # L <= R
        smaller, bigger = LR[0], LR[1]
        left = max(0, i-bigger-1)
        right = i - smaller
        add =  rui[right] - rui[left]
        dp[i] = (dp[i] + add) %mod
    rui[i] = rui[i-1] + dp[i]
    
print(dp[N]%mod)