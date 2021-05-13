from math import ceil
from bisect import bisect

n, a, b = map(int, input().split())
raw_hs = [int(input()) for _ in range(n)]
hs = sorted(raw_hs, reverse=True)
diff = a - b

c_min = 0
c_max = int(10e9)

while c_max - c_min > 1:
	c = (c_min + c_max) // 2
	tmp_hs = [h - c * b for h in hs]
	rem = sum([ceil(h / diff) for h in tmp_hs if h > 0])
	if rem > c:
		c_min = c
	else:
		c_max = c

print(c_max)
