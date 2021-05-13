a, b = list(map(int, input().split()))

if a == b:
	print(a+b)
elif a > b:
	c = a
	a = a - 1
	d = max(a,b)
	c += d 
	print(c)
elif a < b:
	c = b
	b = b - 1
	d = max(a,b)
	c += d 
	print(c)
