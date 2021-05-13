n, y = map(int,raw_input().split())
y/=1000


def g(y,n):
	for a in range(y/10 + 1):
		b,c = f(y - a * 10, n - a)
		if b != -1:
			return [a,b,c]
	return [-1,-1,-1]
def f(y,n):
	if y < 0 or n < 0:
		return [-1,-1]
	if y == 0:
		if n == 0:

			return [0,0]
		return [-1,-1]

	for b in range(y/5 + 1):
		if y - b * 5 == n - b and n - b >= 0:
			return [b,n-b]
	return [-1,-1]

print ' '.join(map(str, g(y,n)))

