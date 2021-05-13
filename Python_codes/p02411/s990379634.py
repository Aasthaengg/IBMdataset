while True:
	m,f,r = map(int,input().split())
	s=m+f
	if r >= 50:
		print('C')
	elif (m == -1) or (f == -1) :
		if(m+f+r == -3):
			break
		else:
			print('F')
	elif s >= 80 :
		print('A')
	elif ((s>=65)&(s<80)):
		print('B')
	elif (s>=50 and s<65):
		print('C')
	elif (s>=30 and s<50):
		print('D')
	elif (s<30):
		print('F')

