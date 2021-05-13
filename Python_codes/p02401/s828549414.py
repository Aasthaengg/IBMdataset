while True:
	a,b,c = map(str,raw_input().split())
	a=int(a)
	c=int(c)
	if b=="+":
		print a+c
	elif b=="-":
		print a-c
	elif b=="*":
	    print a*c
	elif b=="/":
		print a/c
	else:
		break