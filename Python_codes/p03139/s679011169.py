N, A, B = map(int, input().split())
if N>=A+B:
	print(str(min(A, B)) + ' 0')
else:
	print(str(min(A, B)) + ' ' + str(A+B-N))
