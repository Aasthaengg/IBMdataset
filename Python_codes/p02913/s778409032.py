n = int(input())
s = input()
dp = [[0 for i in range(5001)] for j in range(5001)]

for i in range(n-1,-1,-1):
	for j in range(n-1,-1,-1):
		if s[i] != s[j]:
			dp[i][j] = 0
		else:
			dp[i][j] = dp[i+1][j+1] + 1

res = 0
for i in range(n):
	for j in range(n):
		if i >= j:
			continue
		x = min(dp[i][j], j-i)
		res = max(x,res)
print (res)