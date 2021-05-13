n,q=list(map(int,input().split()))
name=[]
time=[]
sum=0
for i in range(n):

	na,ti=input().split()
	name.append(na)
	time.append(int(ti))
	
	
while len(name)>0:
	na=name.pop(0)
	ti=time.pop(0)
	
	if ti>q:
		sum+=q
		name.append(na)
		time.append(ti-q)
		
	else:
		sum+=ti
		print(na, sum)
		
