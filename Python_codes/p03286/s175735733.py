
def f(n):
	if n == 0:
		return '0'
	r = []

	while(n):
		if n % 2:
			r.append(1)
		else:
			r.append(0)
		n = (n-r[-1])/-2
	return ''.join(map(str,r[::-1]))
print f(int(raw_input()))