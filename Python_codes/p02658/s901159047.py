input()
a = list(map(int, input().split()))
if 0 in a:
	print(0)
else:
	if 1 in a:
		a.sort(reverse=True)
		del a[-a.count(1):]
	product = 1
	limit = 10 ** 18
	for x in a:
		product *= x
		if product > limit:
			print(-1)
			break
	else:
		print(product)