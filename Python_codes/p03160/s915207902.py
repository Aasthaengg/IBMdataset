def aminch(dp, pot, dp_1, pot_1): # Absolute MINimum CHanging
	return min(dp, abs(pot-pot_1)+dp_1)

N = int(input())
h = tuple(map(int, input().split()))
dp = [float("INF")]*N
dp[0], dp[1] = 0, abs(h[0]-h[1])

for i in range(2, N):
	dp[i] = aminch(dp[i], h[i], dp[i-1], h[i-1])
	dp[i] = aminch(dp[i], h[i], dp[i-2], h[i-2])

print(dp[-1])