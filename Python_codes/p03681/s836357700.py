import sys
import math
n,m = map(int,input().split())
max = max(n,m)
min = min(n,m)
total = n+m
f_n = math.factorial(n)
f_m = math.factorial(m)
if max - min >= 2:
	print(0)
	sys.exit()
if total%2 == 0:
	ans = f_n*f_m*2
else:
	ans = f_n*f_m
if ans > 10**9+7:
	print(ans%(10**9+7))
else:
	print(ans)