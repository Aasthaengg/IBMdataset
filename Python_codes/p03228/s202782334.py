A,B,K=map(int,input().split())
for i in range(1,K+1):
	if (i%2==1):
		if (A%2==1):
			A=A-1
		A=int(A/2)
		B=B+A
	else:
		if(B%2==1):
			B=B-1
		B=int(B/2)
		A=A+B
print(A,B)