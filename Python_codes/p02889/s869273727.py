import sys

input = sys.stdin.readline
N, M, L = list(map(int,input().split()))
P = [list(map(int,input().split())) for i in range(M)]
Q = int(input())
st = [list(map(int,input().split())) for i in range(Q)]

INF = 100100100100100

dp = [[INF]*N for i in range(N)]
for s,e,d in P:
	if d<=L:
		dp[s-1][e-1] = d
		dp[e-1][s-1] = d
for i in range(N):
	dp[i][i] = 0

for k in range(N):
	for y in range(N):
		for x in range(N):
			dp[y][x] = min(dp[y][x], dp[y][k]+dp[k][x])

dp2 = [[INF]*N for i in range(N)]
for y in range(N):
	for x in range(N):
		if dp[y][x]<=L:
			dp2[y][x] = 1

for k in range(N):
	for y in range(N):
		for x in range(N):
			dp2[y][x] = min(dp2[y][x], dp2[y][k]+dp2[k][x])

for s, t in st:
	count = dp2[s-1][t-1]
	if count==INF:
		print(-1)
	else:
		print(count-1)