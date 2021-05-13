def getlist():
	return list(map(int, input().split()))

INF = float("inf")
N, Ma, Mb = getlist()
L = [[INF] * 401 for i in range(401)]
L[0][0] = 0

#処理
for i in range(N):
	a, b, c = getlist()
	for j in range(401):
		for k in range(401):
			if L[400 - j][400 - k] != INF:
				L[400 - j + b][400 - k + a] = min(L[400 - j][400 - k] + c, L[400 - j + b][400 - k + a])


#最小値
ans = INF
x = Ma
y = Mb
while y <= 400 and x <= 400:
	ans = min(ans, L[y][x])
	x += Ma
	y += Mb

if ans == INF:
	print(-1)
else:
	print(ans)