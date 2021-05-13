a=[]
while True:
	b=input()
	if b==0:
		break
	a.append(b)
i=0
for num in a:
	print 'Case {0}: {1}'.format(i+1,num)
	i+=1