
mod = 10**9+7
n = int(input())
arr = list(map(int , input().split()))
dp = [ [0 for i in range(67)] for j in range(0, n+6)]
for i in range(n-1,0 , -1):
	for j in range( 0 , 61):
		dp[i+1][j]=dp[i+2][j]
	for j in range(0 , 61):
		if (arr[i] &(1<<j)):
			dp[i+1][j]+=1
ans = 0
for i in range(1 , n+1):
	for j in range(0 , 61):
		if (arr[i-1]&(1<<j)):
			ust = n-i-dp[i+1][j]
			ans = ans + (ust*(1<<j))
			ans = ans%mod
		else:
			st = dp[i+1][j]
			ans = ans+(st*(1<<j))
			ans = ans%mod
print(ans)