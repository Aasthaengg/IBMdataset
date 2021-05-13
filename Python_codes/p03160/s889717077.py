N=int(input())
h=list(map(int,input().split()))
dp = [0]*(N)
dp[1]=abs(h[1]-h[0])

for i in range(2,N):
    if i-2 >= 0:
        dp[i] = min(dp[i-1]+abs(h[i-1]-h[i]),dp[i-2]+abs(h[i-2]-h[i]))
    else:
        dp[i] = dp[i-1]+abs(h[i-1]-h[i])
print(dp[N-1])