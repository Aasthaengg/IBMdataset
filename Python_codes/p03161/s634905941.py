
n, k =map(int, input().split())
H=list(map(int, input().split()))

dp = [10**10] * n

dp[0] = 0

dp[1] = abs(H[1] - H[0])
for i in range(2,n):
    for j in range(1,k+1):
        if i-j>=0:
    
            dp[i] = min(dp[i-j] + abs(H[i] - H[i-j]), dp[i])
    
print(dp[-1])