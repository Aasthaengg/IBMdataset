A = input()
B = input()
u = len(A)
v = len(B)
if u>v:
	print("GREATER")
elif v>u:
	print("LESS")
else:
	i , j=0 , 0
	while i<u:
		if A[i]>B[i]:
			print("GREATER")
			exit()
		elif A[i]<B[i]:
			print("LESS")
			exit()
		i=i+1
	print("EQUAL")
	exit()