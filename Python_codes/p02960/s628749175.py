import sys
readline = sys.stdin.readline

def main():

	#s = tuple(input())
	s = input()
	length = len(s)

	dp = [[0]*13 for _ in range(length)]
	MOD = 10**9+7
	if s[-1] == '?':
		for i in range(10):
			dp[0][i] = 1
	else:
		dp[0][int(s[-1])] = 1

	num = 1
	for i in range(1,length):
		num = (10*num) % 13
		if s[-i-1] != '?':
			num2 = num * int(s[-i-1]) % MOD
			for j in range(13):
				dp[i][(num2+j)%13] = dp[i-1][j] % MOD
		else:
			for j in range(10):
				for k in range(13):
					dp[i][(num*j+k)%13] += dp[i-1][k] % MOD

	print(dp[-1][5] % MOD)

if __name__ == '__main__':
	main()
