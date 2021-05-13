N = int(input())
H = list(map(int, input().split()))
H = [0] + H

dp = [None for _ in range(N+1)]

dp[N] = 0
dp[N-1] = abs(H[N]-H[N-1])
for i in range(N-2,0,-1):
	dp[i] = min(abs(H[i+1]-H[i])+dp[i+1], abs(H[i+2]-H[i])+dp[i+2])

print(dp[1])