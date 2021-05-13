def smaller(x, y):
	if x < y: return x
	return y

N, Ma, Mb = map(int, input().split())
a = []
b = []
c = []
suma = 0
sumb = 0
for i in range(0, N):
	inpt = list(map(int, input().split()))
	a.append(inpt[0])
	b.append(inpt[1])
	c.append(inpt[2])
	suma += inpt[0]
	sumb += inpt[1]
dp = []
for i in range(0, N+1):
	lst1 = []
	for j in range(0, suma+1):
		lst2 = []
		for k in range(0, sumb+1):
			lst2.append(-1)
		lst1.append(lst2)
	dp.append(lst1)
dp[0][0][0] = 0
for i in range(0, N):
	for j in range(0, suma+1):
		for k in range(0, sumb+1):
			if dp[i][j][k] != -1:
				if dp[i+1][j][k] == -1:
					dp[i+1][j][k] = dp[i][j][k]
				else:
					dp[i+1][j][k] = smaller(dp[i][j][k], dp[i+1][j][k])
				if dp[i+1][j+a[i]][k+b[i]] == -1:
					dp[i+1][j+a[i]][k+b[i]] = dp[i][j][k] + c[i]
				else:
					dp[i+1][j+a[i]][k+b[i]] = smaller(dp[i][j][k]+c[i], dp[i+1][j+a[i]][k+b[i]])
ans = -1
index = 1
while index * Ma <= suma and index * Mb <= sumb:
	if dp[N][index*Ma][index*Mb] != -1:
		if ans == -1: ans = dp[N][index*Ma][index*Mb]
		else: ans = smaller(ans, dp[N][index*Ma][index*Mb])
	index += 1
print(ans)