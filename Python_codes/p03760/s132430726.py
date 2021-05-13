o=input()
e=input()
a=''
for i in range(len(o)+len(e)):
	if i%2==0:
		a+=o[int(i/2)]
	else:
		a+=e[int((i-1)/2)]
print(a)