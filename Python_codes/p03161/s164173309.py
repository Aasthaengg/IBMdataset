N,K=map(int,input().split())
h=list(map(int,input().split()))
dp = [0]*(N)
for i in range(1,N):
    dp[i] = min(dp[j] + abs(h[j] - h[i]) for j in range(max(0, i - K), i))
print(dp[N-1])