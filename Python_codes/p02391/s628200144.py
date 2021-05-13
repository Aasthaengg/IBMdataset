N = list(map(int, input().split(' ')))
if N[0] < N[1]:
	print('a < b')
elif N[0] > N[1]:
	print('a > b')
else:
	print('a == b')