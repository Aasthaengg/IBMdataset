a = raw_input()
for i, b in enumerate(a.split()):
	if i==0:
		x=int(b)
	elif i==1:
		y=int(b)
	else:
		z=int(b)
if x<y<z:
	print "Yes"
else:
	print "No"