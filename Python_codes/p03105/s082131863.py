import numpy as np
import sys

a, b, c = map(int, input().split())
d = b // a
if d >= c:
	print(c)
else:
	print(d)
