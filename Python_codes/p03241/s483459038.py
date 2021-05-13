n,m = map(int,raw_input().split())

def f(n,m):
	if n == 1:
		return m
	divisors = []
	for d in range(2, int(m ** 0.5)+1)[::-1]:
		if m % d == 0:
			divisors.append(d)
			if d != m/d: divisors.append(m/d)
	divisors.sort(key = lambda x:-x)
	for d in divisors:
		if m/d >= n:
			return d

	return 1

print f(n,m)