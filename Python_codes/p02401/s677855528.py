n=0
l= []
while True:
	X,op,Y= input().split()
	x= int(X)
	y= int(Y)
	if(op== '?'):
		break
	elif(op== '+'):
		l.append(x+y)
	elif(op== '*'):
		l.append(x*y)
	elif(op== '-'):
		l.append(x-y)
	elif(op== '/'):
		l.append(x//y)
	n+=1
for i in range(n):
	print(l[i])