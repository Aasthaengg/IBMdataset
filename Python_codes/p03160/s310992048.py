N = int(input())
H = list(map(int, input().split()))
H = [0] + H
dp = [0] * (N+1)
for i in range(2,N+1):
    if i-2>=1:
        dp[i] = min(dp[i-1]+abs(H[i]-H[i-1]), dp[i-2]+abs(H[i]-H[i-2]))
    else:
        dp[i] = dp[i] + abs(H[i]-H[i-1])
res = dp[N]
print(res)