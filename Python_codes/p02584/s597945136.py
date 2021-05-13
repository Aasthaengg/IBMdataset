position,moves,distance=[int(x) for x in input().split()]
position=abs(position)
if position>=distance*moves:
	print(abs(position-distance*moves))
else:
	variable=moves-position//distance
	if variable%2==0:
		print(abs((position-distance*(position//distance))))
	else:
		print(abs(position-distance*((position//distance) + 1)))