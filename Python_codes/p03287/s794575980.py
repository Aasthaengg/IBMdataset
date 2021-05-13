from itertools import accumulate
from collections import defaultdict

n, m = map(int, input().split())
a = list(map(int, input().split()))

acm = [0] + list(accumulate(a))
d = defaultdict(int)

for e in acm:
	r = e % m
	d[r] += 1

ans = 0
for v in d.values():
	ans += v * (v - 1) // 2

print(ans)
