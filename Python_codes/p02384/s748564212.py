d=list(map(int,input().split()))
for i in range(int(input())):
	o=list(map(int,input().split()))

	for i in range(4):
		 d[0],d[1],d[4],d[5]=d[1],d[5],d[0],d[4]
		 if d[0]==o[0]:
		 	break
	if d[0]!=o[0]:
		for i in range(4):
			d[0],d[3],d[5],d[2]=d[3],d[5],d[2],d[0]
			if d[0]==o[0]:
				break
	for i in range(4):
		d[1],d[3],d[4],d[2]=d[3],d[4],d[2],d[1]
		if d[1]==o[1]:
			break
	print(d[2])
	
