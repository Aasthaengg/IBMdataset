N = int(input())
a = False
for i in range(1, 10):
	if N % i == 0:
		if N // i <= 9:
			a = True
			break
if a:
	print('Yes')
else:
	print('No')

