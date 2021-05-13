w,a,b = map(int, raw_input().split())

def f(a,b,w):
	if a > b:
		return f(b,a,w)
	return max(0, b - (a + w))

print f(a, b,w)