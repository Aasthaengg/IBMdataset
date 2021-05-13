h,n = map(int,input().split())
mahou = []
for i in range(n):
	a,b = map(int,input().split())
	mahou.append((a,b))
dp = [10**18 for _ in range(h+1)]
dp[0] = 0
for i in range(h+1):
	for j, k in mahou:
		if j+i <= h:
			dp[j+i] = min(dp[i]+k, dp[j+i])
		else:
			dp[h] = min(dp[i]+k, dp[h])
print(dp[h])