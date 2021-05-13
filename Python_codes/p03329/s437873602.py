INF = 10 ** 20
 
N = int(input())
coin_list = [1] + [6**i for i in range(1, 7)] + [9**i for i in range(1, 6)]
dp = [INF]*(N+1)
dp[0] = 0
 
for amount in range(1,N+1):
	for coin in coin_list[::-1]:
	    if amount-coin >= 0: dp[amount] = min(dp[amount], dp[amount-coin]+1)
 
print(dp[N])