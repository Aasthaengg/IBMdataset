import sys
input = sys.stdin.readline

N,K   = map(int,input().split())
lst_a = list(map(int, input().split()))

dp= [-1 for i in range(K+1)]
dp[0] = 0
for i in range(1,K+1):
	check = False
	for j in lst_a:
		if(i-j>=0):
			if (dp[i-j] == 0):
				check = True
	if(check): dp[i]= 1
	else : dp[i]= 0

if(dp[K]==1):
	print("First")
else:
	print("Second")