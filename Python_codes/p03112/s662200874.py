nim, mike, kite = map(int, input().split())

INF = 10 ** 11 + 1
S = [-INF] + [int(input()) for _ in range(nim)] + [INF]
T = [-INF] + [int(input()) for _ in range(mike)] + [INF]
X = [int(input()) for _ in range(kite)]

def bsr(a, v):
	lo, hi = 0, len(a)
	while lo < hi:
		mid = (lo + hi) // 2
		if x < a[mid]: hi = mid
		else: lo = mid + 1
	return lo

for x in X:
	sr = bsr(S, x)
	sl = sr - 1
	tr = bsr(T, x)
	tl = tr - 1
	cost = []
	for m in [S[sr], S[sl]]:
		for n in [T[tr], T[tl]]:
			cost += [abs(x - m) + abs(m - n), abs(x - n) + abs(m - n)]
	print(min(cost))
