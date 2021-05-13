import sys

import numpy as np
from collections import deque
from collections import Counter
from itertools import accumulate
from itertools import permutations, combinations
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from math import ceil, floor, sqrt
### ceil切り上げ，floor切り下げ

def main():
	n, x = map(int, input().split())
	lst = list(map(int, input().split()))
	d = 0
	ans = 1
	for l in lst:
		d += l
		if d <= x:
			ans += 1
		else:
			break
	print(ans)


if __name__ == '__main__':
	main()