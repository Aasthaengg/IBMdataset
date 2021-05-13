def f(k,a,b,t):
	if k == 0:
		return t
	

	if t >= a:
		if b-a > 2 and k >= 2:
			return f(k%2, a,b,t + k/2 * (b-a))
		else:
			return f(0, a, b, t + k)
	else:
		dist=  a-t
		return f(k-min(k,dist), a, b, t + min(k,dist))

k,a,b = map(int, raw_input().split())
print f(k,a,b,1)