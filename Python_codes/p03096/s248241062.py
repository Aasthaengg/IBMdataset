MOD = 1000000007

N = int(input())
C = [int(input()) for _ in range(N)]

prev = [None for _ in range(max(C)+1)]
dp = [0 for _ in range(N+1)]
dp[0] = 1

for i in range(N):
    if prev[C[i]] is None or prev[C[i]]==i:
        dp[i+1] = dp[i]
    else:
        dp[i+1] = dp[i] + dp[prev[C[i]]]
    dp[i+1] %= MOD
    prev[C[i]] = i+1
    
print(dp[N])