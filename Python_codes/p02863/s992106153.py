N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key = lambda x: x[0])

DP = [[0] * T for _ in range(N-1)]

for i in range(N-1):
	for j in range(T):
		if i == 0:
			if j >= AB[0][0]:
				DP[i][j] = AB[0][1]
		else:
			if j >= AB[i][0]:
				DP[i][j] = max(DP[i-1][j], DP[i-1][j-AB[i][0]] + AB[i][1])
			else:
				DP[i][j] = DP[i-1][j]

ans = 0
tmp = 0

for i in reversed(range(N-1)):
	tmp = max(tmp, AB[i+1][1])
	ans = max(ans, DP[i][T-1] + tmp)

print(ans)