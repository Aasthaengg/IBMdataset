a,b = map(int,raw_input().split(' '))
while(True):
	if(a == b):
		print a
		break
	if(a < b):
		t = a
		a = b
		b = t
	a,b = b,a%b
	if(b == 0):
		print a
		break