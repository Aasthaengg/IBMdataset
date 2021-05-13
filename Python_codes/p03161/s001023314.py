n,k = map(int,input().split())
if n <= k:
    k = n
H = list(map(int,input().split()))
dp = [float('inf') for _ in range(n+1)]
for i in range(k):
    dp[i] = abs(H[i] - H[0])
for i in range(k,n):
    for j in range(k+1):
        dp[i] = min(dp[i],dp[i-j] + abs(H[i] - H[i-j]))
print(dp[-2])