while True:
	p=list(map(int,input().split()))
	if p[0]==-1 and p[1]==-1 and p[2]==-1:
		break
	else:
		if p[0]==-1 or p[1]==-1:
			print('F')
		elif p[0]+p[1]>=80:
			print('A')
		elif 65<=p[0]+p[1]<80:
			print('B')
		elif 50<=p[0]+p[1]<65:
			print('C')
		elif 30<=p[0]+p[1]<50:
			if p[2]>=50:
				print('C')
			else:
				print('D')
		else:
			print('F')
	
