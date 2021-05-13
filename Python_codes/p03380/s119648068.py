N = int(input())
L = list(map(int, input().split()))
L = sorted(L)

import math
import bisect
max = L[-1]
maxdiv2 = max//2
posleft = bisect.bisect_left(L, maxdiv2)
posright = bisect.bisect_right(L, maxdiv2)

if len(L) == 2:
	print(L[1], L[0])
	exit()

if posleft!= posright:
	print(max, L[posleft])
	exit()

if abs(max/2 - L[posleft]) > abs(max/2 - L[posleft-1]):
	print(max, L[posleft-1])
else:
	print(max, L[posleft])