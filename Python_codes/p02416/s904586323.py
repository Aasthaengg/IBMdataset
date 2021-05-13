while(1):
	a=int(input())
	if a==0:
		break 
	a=list(map(int,list(str(a))))
	print(sum(a))