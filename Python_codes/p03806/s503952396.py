def smaller(x, y):
	if x < y:
		return x
	return y

N, Ma, Mb = map(int, input().split())
dp = []
for i in range(0, 401):
	lst = []
	for j in range(0, 401):
		lst.append(-1)
	dp.append(lst)
dp[0][0] = 0
for i in range(0, N):
	a, b, c = map(int, input().split())
	next = []
	for j in range(0, 401):
		for k in range(0, 401):
			if dp[j][k] != -1:
				if dp[j+a][k+b] == -1:
					next.append([j+a, k+b, dp[j][k]+c])
				else:
					if dp[j][k]+c == smaller(dp[j+a][k+b], dp[j][k]+c):
						next.append([j+a, k+b, dp[j][k]+c])
	for j in range(0, len(next)):
		if next[j][0] <= 400 and next[j][1] <= 400:
			dp[next[j][0]][next[j][1]] = next[j][2]
min = 5000000000000000
index = 1
while Ma*index <= 400 and Mb*index <= 400:
	if dp[Ma*index][Mb*index] != -1:
		min = smaller(min, dp[Ma*index][Mb*index])
	index += 1
if min == 5000000000000000:
	print(-1)
else:
	print(min)