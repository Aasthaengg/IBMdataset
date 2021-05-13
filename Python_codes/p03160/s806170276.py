N = int(input())
h = [int(i) for i in input().split()]
dp = [10**4+1] * N

dp[0] = 0
dp[1] = abs(h[1]-h[0])

for i in range(2,N) :
    a = dp[i-2]+abs(h[i-2]-h[i])
    b = dp[i-1]+abs(h[i-1]-h[i])
    dp[i] = min(a,b)

print(dp[-1])