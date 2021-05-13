n=input()
N=int(n)

f=True
c=int(n[0])
if len(n)==1:
	x=N
else:
	for i in range(1, len(n)):
		if int(n[i]) != 9:
			f=False
	
	if f:
		x=c+9*(len(n)-1)
	else:
		x=c+9*(len(n)-1)-1

print(x)