n=int(input())
man=list(map(int,input().split()))
can=[]
for i in range(1,101):
	pp=0
	for j in range(len(man)):
		bp=(man[j]-i)**2
		pp+=bp
	can.append(pp)
can.sort(key=int)
print(can[0])
