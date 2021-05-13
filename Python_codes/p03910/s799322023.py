N=int(input())
for i in reversed(range(1,10001)):
	if N<=(i*(i-1)//2) and N>(i-1)*(i-2)//2:
		print(i-1)
		N-=(i-1)
	else:continue