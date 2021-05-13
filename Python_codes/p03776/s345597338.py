from operator import mul
from functools import reduce

def cmb(n, r):
	if n < r: return 0
	if r == 0 or n - r == 0: return 1
	r = min(n - r, r)
	u = reduce(mul, range(n, n - r, -1))
	d = reduce(mul, range(1, r + 1))
	return u // d

n,a,b,*v=map(int,open(0).read().split())
v.sort(reverse=True)
print(sum(v[:a])/a)
c=v[a-1]
cnt=v.count(c)
d=sum(x>c for x in v)
if d:
	print(cmb(cnt,a-d))
else:
	print(sum(cmb(cnt,i) for i in range(a,min(cnt,b)+1)))