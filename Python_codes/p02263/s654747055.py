a=[]
for i in input().split():
	if i=='+':
		a[len(a)-2]=int(a[len(a)-2])+int(a[len(a)-1])
		a.pop()
	elif i=='-':
		a[len(a)-2]=int(a[len(a)-2])-int(a[len(a)-1])
		a.pop()
	elif i=='*':
		a[len(a)-2]=int(a[len(a)-2])*int(a[len(a)-1])
		a.pop()
	else :
		a.append(i)

print(a[0])
