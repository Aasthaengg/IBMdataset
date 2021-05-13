N, M = map(int, input().split())
ab = tuple(tuple(a for a in map(int, input().split())) for _ in range(N))
cd = tuple(tuple(a for a in map(int, input().split())) for _ in range(M))
for i in range(N):
	ckp = 1
	dist_min = 10**9
	for j in range(M):
		dist = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
		if dist < dist_min:
			dist_min = dist
			ckp = j + 1
	print(ckp)