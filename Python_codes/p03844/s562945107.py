a=input()
for i in range(len(a)):
	if a[i]=='+':
		a1=int(a[:i])
		a2=int(a[i+1:])
		print(a1+a2)
	elif a[i]=='-':
		a1=int(a[:i])
		a2=int(a[i+1:])
		print(a1-a2)

		
