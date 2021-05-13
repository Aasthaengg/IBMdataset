n = int(raw_input())
a = map(int, raw_input().split())
sm = 0
h = len(a) / 2

while h > 0:
	for x in xrange(0,len(a)):
		y = x
		tmp = a[y]
		while y - h >= 0 and a[y-h] > tmp:
			a[y] = a[y-h]
			y = y - h
		a[y] = tmp
		
	if h == 1:
		h = 0
	elif h / 2 != 0:
		h = h / 2
	else:
		h = 1

for x in xrange(0,len(a)):
	sm = sm + a[x]

print a[0], a[len(a)-1], sm