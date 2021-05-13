while True:
	a = input()
	if a=='-':
		exit(0)
	b = int(input())
	for i in range(0,b):
		c = int(input())
		a = a[c:]+a[:c]
	print(a)
