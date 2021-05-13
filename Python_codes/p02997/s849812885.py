N,K=[int(x) for x in input().split()]
if K>(N-2)*(1+N-2)//2:
	print(-1)
else:
	print(((N-2)*(1+N-2)//2)+((N-1)-K))
	counter=0
	for i in range(2,N+1):
		print(1,i)
		counter+=1
	for i in range(2,N+1):
		for j in range(i+1,N+1):
			if counter==((N-2)*(1+N-2)//2)+((N-1)-K):
				exit()
			else:
				print(i,j)
				counter+=1