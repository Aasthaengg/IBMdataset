ab = [int(i) for i in input().split()]

if all(i <= 8 for i in ab):
	print('Yay!')
else:
	print(':(')