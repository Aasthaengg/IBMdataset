a=input().split()
b=[]
for i in range(len(a)):

	if a[i]=="+":

		b[len(b)-2]=b[len(b)-2]+b[len(b)-1];
		del b[len(b)-1]

	elif a[i]=="-":

		b[len(b)-2]=b[len(b)-2]-b[len(b)-1];
		del b[len(b)-1]

	elif a[i]=="*":

		b[len(b)-2]=b[len(b)-2]*b[len(b)-1];
		del b[len(b)-1]

	else:
		b.append(int(a[i]))

		
print(b[len(b)-1])
