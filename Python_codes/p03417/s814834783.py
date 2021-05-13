n,m = map(int, raw_input().split())
def f(a,b): 
	if a == 1 and b == 1:
		return 1
	if a == 1 or b == 1:
		return max(0, max(a,b) - 2)
	return max(0,a - 2) * max(0, b - 2) 
print f(n,m)