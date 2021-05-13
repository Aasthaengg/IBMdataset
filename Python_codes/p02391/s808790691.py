a = raw_input()
for i, b in enumerate(a.split()):
	if i==0:
		x=int(b)
	else:
		y=int(b)
if x==y:
	print "a == b"
elif x>y:
	print "a > b"
else:
	print "a < b"