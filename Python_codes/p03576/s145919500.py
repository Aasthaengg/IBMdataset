from collections import defaultdict

N, K = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(N)]
INF = 10 ** 19

acc = defaultdict(int)

x = [-INF]
y = [-INF]

for ex, ey in xy:
	acc[(ex, ey)] = 1
	x.append(ex)
	y.append(ey)

x.sort()
y.sort()

for i in range(N):
	for j in range(N + 1):
		acc[(x[i+1], y[j])] += acc[(x[i], y[j])]

for j in range(N):
	for i in range(N + 1):
		acc[(x[i], y[j+1])] += acc[(x[i], y[j])]

ans = INF
for i in range(1, N + 1):
	for j in range(i + 1, N + 1):
		for k in range(1, N + 1):
			for l in range(k + 1, N + 1):
				cnt = acc[(x[j], y[l])] - acc[(x[j], y[k-1])] - acc[(x[i-1], y[l])] + acc[(x[i-1], y[k-1])]
				if cnt >= K:
					sq = (x[j] - x[i]) * (y[l] - y[k])
					ans = min(ans, sq)

print(ans)
