A= input()
if len(A)== 1:
	print(A)
	exit()
length=len(A)
B = "9" * (length-1)
A=int(A)
C=A-int(B)
B=str(int(C/10**(length-1)))+B
B=int(B)
B=list(str(B))
B=list(map(int,B))
print(sum(B))