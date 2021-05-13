n, k = map(int, input().split())
h = list(map(int, input().split()))

inf = 10**10
dp = [0] + [inf] * (n-1)

for i in range(1,n):
    j = 1
    while j <= k and j <= i:
        dp[i] = min(dp[i-j]+abs(h[i]-h[i-j]), dp[i])
        j += 1
    
print(dp[-1])