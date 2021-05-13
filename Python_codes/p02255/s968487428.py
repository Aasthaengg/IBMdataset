N = input();
A = map(int,raw_input().split(" "))
for i in range(1,len(A)):
	key = A[i]
	j = i - 1;
	for k in range(0,len(A)):
		if A[N-1] == A[k]:
			print A[k]
		else:
			print A[k],
	while j >=0 and A[j] > key:
		A[j+1] = A[j]
		j -= 1
	A[j+1] = key
for j in range(0,len(A)):
		if A[N-1] == A[j] :
			print A[j]
		else:
			print A[j],