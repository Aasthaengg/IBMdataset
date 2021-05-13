while True:
	a=0
	num=list(map(int,input().split()))
	if num[0]==0 and num[1]==0:
		break
	else:
		for i in range(1,num[0]+1):
			for j in range(i+1,num[0]+1):
				for k in range(j+1,num[0]+1):
					if i+j+k==num[1]:
						a+=1
		print(a)
					
			
