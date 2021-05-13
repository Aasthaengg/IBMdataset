n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]
s = max(w)-1
w.append(10**13)
t = sum(w)

while s+1 < t:
	m = (s + t) // 2
	x = 0
	c = 0
	for i in range(n+1):
		c += w[i]
		if c > m:
			x += 1
			c = w[i]
		elif c == m:
			if i != n-1:
				x += 1
				c = 0
	if x > k:
		s = m
	else:
		t = m

print(t)
