n,q = map(int,raw_input().split(' '))
s = raw_input()
dp = [0] * len(s)
cumul = 0
for j in range(len(s)):
	if s[j - 1:j + 1] == 'AC': cumul +=1
	dp[j] = cumul 
"""
ac ac
 ^
    ^    
"""
for _ in range(q):
	u,v = map(int, raw_input().split(' '))
	u -=1
	v -=1
	print dp[v] - dp[u]
