N,K = map(int,input().split())

h = list(map(int,input().split()))

INF = 100100100100100
dp = [INF]*N

dp[0] = 0

for i in range(1,N):
    for k in range(1,K+1):
        if i < k:
            break
        dp[i] = min(dp[i], dp[i-k] + abs(h[i] - h[i-k]))
        
print(dp[N-1])