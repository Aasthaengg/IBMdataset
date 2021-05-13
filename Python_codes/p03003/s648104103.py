import collections
n,m = map(int, raw_input().split(' '))
s,t = map(int, raw_input().split(' ')), map(int, raw_input().split(' '))
dp,prefix = [[0 for j in range(len(t))] for i in range(len(s))], [[0 for j in range(len(t))] for i in range(len(s))]
total = 1
mod = (10 ** 9) + 7
for ii in range(len(s)):
	for jj in range(len(t)):
		if s[ii] == t[jj]:
			dp[ii][jj] = 1+ (prefix[ii-1][jj-1] if ii-1>=0 and jj-1>=0 else 0)
			total += dp[ii][jj]
			total %= mod
		prefix[ii][jj] += prefix[ii - 1][jj] if ii - 1 >=0 else 0
		prefix[ii][jj] += prefix[ii][jj - 1] if jj - 1 >=0 else 0
		prefix[ii][jj] -= prefix[ii - 1][jj - 1] if (jj - 1 >=0) and (ii-1) >=0 else 0
		prefix[ii][jj] += dp[ii][jj]
		prefix[ii][jj] %= mod
		
print total
