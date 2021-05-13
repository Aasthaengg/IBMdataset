N=int(input())
if N%2==0:
	print(int((N-2)*N/2))
	for i in range(N):
		for j in range(i+1,N):
			if  (i+j+2 != N+1):
				print(i+1,j+1)
else:
	print(int((N-3)*(N-1)/2)+(N-1))
	for i in range(N-1):
		for j in range(i+1,N-1):
			if  (i+j+2 != N):
				print(i+1,j+1)
		print(i+1,N)
