def cornerval(i, j, a, dp, h, w):

	if a[i][j] == '#':
		return 0
	elif(j== w-1):
		if(dp[i+1][j] == 0):
			return 0
		else:
			return 1
	elif(i==h-1):
		if(dp[i][j+1] == 0):
			return 0
		else:
			return 1

l = 10**9 + 7
h, w = map(int, raw_input().split())
a = []
for i in range(h):
	t= raw_input()
	t = list(t)
	a.append(t)
# print(a)
dp=[[0 for x in range(w)] for x in range(h)]
dp[h-1][w-1] = 1
i=h-1
for j in range(w-2, -1, -1):
	dp[i][j] = cornerval(i, j, a, dp, h, w)
j = w-1
for i in range(h-2, -1, -1):
	dp[i][j] = cornerval(i, j, a, dp, h, w)
dp[h-1][w-1] = 0


for i in range(h-2, -1, -1):
	for j in range(w-2, -1, -1):
		if(a[i][j] == '#'):
			dp[i][j] = 0
		else:
			dp[i][j] = ((dp[i+1][j] % l) + (dp[i][j+1] % l)) % l
# for i in dp:
# 	print(i)
print(dp[0][0])