N,A,B=map(int,input().split(" "))
if N-A-B>0:
	W=0
else:
    W=A+B-N
print(min(A,B),W)