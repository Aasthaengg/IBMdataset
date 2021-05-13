L=list(map(int,input().split()))
A=abs(L[0]-L[1])
B=abs(L[0]-L[2])
if min(A,B)==A:
	print("A")
else:
	print("B")