d=list(map(int,input().split()))
o=[]
for i in input():
	o.append(i)
for i in range(len(o)):
	if o[i]=='N':
		d[0],d[1],d[4],d[5]=d[1],d[5],d[0],d[4]
	elif o[i]=='S':
		d[0],d[4],d[5],d[1]=d[4],d[5],d[1],d[0]
	elif o[i]=='E':
		d[0],d[3],d[5],d[2]=d[3],d[5],d[2],d[0]
	elif o[i]=='W':
		d[0],d[2],d[5],d[3]=d[2],d[5],d[3],d[0]
print(d[0])
	
