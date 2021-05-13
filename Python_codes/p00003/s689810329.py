rep = input()
while rep:
	rep -= 1
	[a, b, c] = map(int, raw_input().split())
	if b < a and c < a:
		a **= 2
		b = b ** 2 + c ** 2
	elif a < b and c < b:
		a = a ** 2 + c ** 2	
		b **= 2
	else:
		a = a ** 2 + b ** 2
		b = c ** 2
	if a == b:
		print 'YES'
	else:
		print 'NO'