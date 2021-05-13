n=int(input())
A=0
B=0
for i in range(n):
	a,b=input().split()
	if a>b:
		A+=3
	elif a==b:
		A+=1
		B+=1
	else:
		B+=3
print(A,B)