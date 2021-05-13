h1, m1, h2, m2, k = map(int, input().split())
h = h2 - h1
if m1>m2:
	h-=1
	m = m2 - m1 + 60
else:
	m = m2 - m1
l = h*60 + m - k
print(l)