import sys
input = sys.stdin.readline

N = int(input())
prob_table = list(map(float, input().split()))

dp = [[0 for _ in range(2*N+2)] for _ in range(N)]


dp[0][N-1] = 1 - prob_table[0]
dp[0][N+1] =   prob_table[0]

for i in range(1,N):
	for j in range(N-i-1,N+i+2):
		if(j > 0 and j < 2*N+1):
			dp[i][j] = dp[i-1][j-1]*prob_table[i] + dp[i-1][j+1]*(1-prob_table[i])
		elif(j <= 0):
			dp[i][j] = dp[i-1][j+1]*(1-prob_table[i])
		else : 
			dp[i][j] = dp[i-1][j-1]*prob_table[i]
print(sum(dp[N-1][N+1:]))