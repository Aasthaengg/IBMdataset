import sys
input = sys.stdin.readline
from bisect import bisect_left

n, d, a = map(int, input().split())
mon = [list(map(int, input().split())) for _ in range(n)]
mon.sort(key=lambda x: x[0])
ref = [x for x, h in mon]
rem = [0] * (n + 1)
ans = 0
cur = 0
for i, (x, h) in enumerate(mon):
	cur -= rem[i]
	h = max(0, h - cur)
	t = a * (0 - -h // a)
	ans += 0 - -h // a
	cur += t
	rem[bisect_left(ref, x + 2 * d + 1)] += t
print(ans)