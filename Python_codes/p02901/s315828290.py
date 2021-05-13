N, M = map(int, input().split())
a,c = [], []
for _ in range(M):
	ta, _ = map(int, input().split())
	tc = 0
	tmp = list(map(int, input().split()))
	for t in tmp:
		tc += 1 << (t-1)

	a.append(ta)
	c.append(tc)

inf = float('inf')

DP = [[inf] * (1 << N) for _ in range(M)]
for i in range(M):
	DP[i][0] = 0
DP[0][c[0]] = a[0]

for i in range(1, M):
	for s in range(1 << N):
		DP[i][s] = min(DP[i][s], DP[i-1][s])
		DP[i][s | c[i]] = min(DP[i][s|c[i]], DP[i-1][s|c[i]], DP[i-1][s]+a[i])

ans = DP[M-1][(1 << N)-1]
if ans == inf:
	print(-1)
else:
	print(ans)