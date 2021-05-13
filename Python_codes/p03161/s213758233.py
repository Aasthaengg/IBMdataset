I = list(map(int, input().split()))
N = I[0]
K = I[1]
H = list(map(int, input().split()))

dp = [float('inf') for _ in range(N+1)]

dp[N] = 0
for i in range(N-1,N-K-1,-1):
	if i>0:
		dp[i] = abs(H[i-1]-H[N-1])

for i in range(N-K-1,0,-1):
	for k in range(1,K+1):
		if i+k<=N:
			dp[i] = min(abs(H[i+k-1]-H[i-1])+dp[i+k], dp[i])

print(dp[1])