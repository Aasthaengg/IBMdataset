m = 0
f = 0
r = 0
while m!=-1 or f!=-1 or r!=-1:
	m,f,r = [int(i) for i in input().split()]
	sum = m + f
	if m!=-1 or f!=-1 or r!=-1:
		if m == -1 or f == -1:
			print('F')
		elif sum >= 80:
			print('A')
		elif sum >= 65:
			print('B')
		elif sum >= 50:
			print('C')
		elif sum >= 30:
			if r >= 50:
				print('C')
			else:
				print('D')
		else:
			print('F')