N=int(input())
for i in range(1,3501):
	for j in range(1,3501):
		if ((4*i*j)-(N*i)-(N*j))>0:
			if (i*j*N)%((4*i*j)-(N*i)-(N*j))==0:
				k=(i*j*N)//((4*i*j)-(N*i)-(N*j))
				print(i,j,k)
				exit()