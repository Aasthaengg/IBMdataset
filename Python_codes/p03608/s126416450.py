import itertools
import sys

N, M, R = map(int, input().split())
r = [int(i) for i in input().split()]
r.sort()
a = [[sys.maxsize] * N for i in range(N)]
for i in range(M):
	A, B, C = map(int, input().split())
	a[A - 1][B - 1] = C
	a[B - 1][A - 1] = C
for i in range(N):
	a[i][i] = 0
for i in range(N):
	for j in range(N):
		if a[j][i] == sys.maxsize:
			continue
		for k in range(N):
			if a[i][k] == sys.maxsize:
				continue
			a[j][k] = min(a[i][k] + a[j][i], a[j][k])
ans = sys.maxsize
for i in itertools.permutations(r):
	b, j = 0, 1
	while j < R:
		b += a[i[j - 1] - 1][i[j] - 1]
		j += 1
	ans = min(b, ans)
print(ans)