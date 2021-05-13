a, b, c= input().split()
a, b, c= int(a), int(b), int(c)

eq= b+c
eq2= a-b
eq3= c-eq2

if eq < a:
	print('0')
else :
	print(eq3)