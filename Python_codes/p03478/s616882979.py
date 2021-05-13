
n, a, b = map(int , raw_input().split())
def dfs(u, q, n, a, b):
	c = 0
	if u > n:return 0

	if a <= q <= b: 
		c += u

	for d in range(0 if u else 1,10): 
		c += dfs(u * 10 + d,q + d, n, a, b)
	return c


print dfs(0, 0,n, a, b )