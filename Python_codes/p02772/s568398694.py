N = int(input())
A = list(map(int, input().split()))
a = True
for x in A:
	if x % 2 == 0:
		if x % 3 != 0 and x % 5 != 0:
			a = False
			break
if a:
	print('APPROVED')
else:
	print('DENIED')
