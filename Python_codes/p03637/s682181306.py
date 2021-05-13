def resolve():
	n = int(input())
	div4 = 0
	div2 = 0
	divn = 0
	for i in list(map(int, input().split())):
		if i % 4 == 0:
			div4 += 1
		else:
			if i % 2 == 0:
				div2 += 1
			else:
				divn += 1
	if div2:
		divn += 1
	if div4 + 1 >= divn:
		print('Yes')
	else:
		print('No')
resolve()