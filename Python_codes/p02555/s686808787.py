dp = [-1 for i in range(2005)]
dp[0] = 0

def ok(s):
	if s==0:
		return 1
	elif s==1 or s==2:
		return 0
	elif s>=3 and s<=5:
		return 1
	elif dp[s] != -1 :
		return dp[s]
	else:
		total = 0
		for i in range(3,s+1):
			if s-i >=0 :
				total = total + ok(s-i)

		dp[s]=total

		return total



s = int(input())
print(ok(s)%((10**9) + 7))