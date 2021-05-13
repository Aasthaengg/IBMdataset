# thought greedy was better i am noob
# classical problem no explanation needed
def main():
	n = int(input())
	dp = [0 for i in range(n+4)]
	dp[0]=0
	for i in range(1, n+2):
		p = 1
		dp[i]=1000000000000000
		while i>=p:
			dp[i]=min(dp[i] , dp[i-p]+1)
			p =p*9
		p=1
		while i>=p:
			dp[i]=min(dp[i] , dp[i-p]+1)
			p = p*6
	print(dp[n])
if __name__=="__main__":
	main()