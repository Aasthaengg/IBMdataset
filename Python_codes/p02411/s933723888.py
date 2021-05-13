while 1 :
	m,f,r = map(int , raw_input().split())
	
	s = m + f
	
	if m == f == r == -1 :
		break
	elif m == -1 or f == -1 or s < 30 :
		print "F"
	elif s >= 80 :
		print "A"
	elif s >= 65 :	
		print "B"
	elif s >= 50 : 
		print "C"
	elif s >= 30 and r >= 50 :
		print "C"
	else :
		print "D"