a, b, c, d, e, f = map(int, input().split())
w = []
for i in range(f//100+1):
	for j in range(f//100+1):
		x = a*i*100+b*j*100
		if x > 0 and x <= f:
			w.append(x)
w.sort()
s = []
for i in range(f//c+1):
	for j in range(f//d+1):
		if  c*i+(c*i)*e/100 + d*j+(d*j)*e/100 <= f:
			s.append(c*i + d*j)
s.sort(reverse=True)
c = -1.0
for i in w:
	for j in s:
		if i+j <= f and j <= i*e/100:
			if c < 100*j/(i+j):
				c = 100*j/(i+j)
				g, h = i+j,j
print(g,h)