mod = 10**9+7
n = int(input())
C = []
prev = None
for i in range(n):
	tmp = int(input())
	if tmp==prev:
		n -= 1
		continue
	else:
		C.append(tmp)
		prev = tmp
dp = [0]*n
dp[0] = 1
table = {C[0]:1}

for i in range(n-1):
	if C[i+1] not in table:
		table[C[i+1]]= 0 
	dp[i+1] = dp[i] + table[C[i+1]]  
	table[C[i+1]] += dp[i]
	dp[i+1] %= mod
	table[C[i+1]] %= mod

print(dp[n-1])
