a = raw_input()
for i, b in enumerate(a.split()):
	if i==0:
		x=int(b)
	elif i==1:
		y=int(b)
	else:
		z=int(b)
if x<=y<=z:
	print x,y,z
elif x<=z<=y:
	print x,z,y
elif y<=x<=z:
	print y,x,z
elif y<=z<=x:
	print y,z,x
elif z<=x<=y:
	print z,x,y
else:
	print z,y,x