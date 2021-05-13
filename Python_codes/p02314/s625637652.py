n, m = map(int, input().split())
coin = list(map(int, input().split()))
    
#dp = [[0]*(w+1) for _ in range(n+1)]
#dp[0] = [0]*(w+1)
dp = [999999]*(n+1)
dp[0] = 0

for i in range(1, n+1):
    dp[i] = min([dp[i-coin[j]]+1 if i-coin[j]<n and i-coin[j]>=0 else 999999 for j in range(m)])

            
print(dp[n])
