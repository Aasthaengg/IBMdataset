while True:
	sum = 0
	A = input()
	if int(A) == 0 : break
	for i in range(len(A)):
		sum += int(A[i])
	print(sum)

