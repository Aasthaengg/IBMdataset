while True:
	pt=map(int,raw_input().split(" "))
	if pt[0]==-1 and pt[1]==-1 and pt[2]==-1:
		break
	elif pt[0]==-1 or pt[1]==-1:
		print "F"
	elif pt[0]+pt[1]>=80:
		print "A"
	elif 65<=pt[0]+pt[1]<80:
		print "B"
	elif 50<=pt[0]+pt[1]<65:
		print "C"
	elif 30<=pt[0]+pt[1]<50 and pt[2]<50:
		print "D"
	elif 30<=pt[0]+pt[1]<50 and pt[2]>=50:
		print "C"
	elif pt[0]+pt[1]<30:
		print "F"