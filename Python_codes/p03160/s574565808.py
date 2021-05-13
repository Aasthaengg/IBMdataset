n = int(input())
H = list(map(int,input().split()))
dp = [0 for _ in range(n+1)]
dp[1] = abs(H[1] - H[0])
for i in range(2,n):
    b1 = dp[i-1] + abs(H[i] - H[i-1])
    b2 = dp[i-2] + abs(H[i] - H[i-2])
    dp[i] = min(b1,b2)
print(dp[-2])