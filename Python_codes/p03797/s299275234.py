n, m = map(int, raw_input().split())
def f(n,m): 
	if n == 0:
		return m /4


	x = min(n, m/2)
	if x:
		return x + f(n - x,m - 2*x)
	else:
		return 0
print f(n,m)