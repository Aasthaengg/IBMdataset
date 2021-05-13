'''input
31 10
'''
import time
import math
n, k = map(int, input().strip().split())
d = (n + 1) / 2
if k <= d:
	print("YES")
else:
	print("NO")