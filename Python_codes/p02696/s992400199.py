A,B,N =list(map(int,input().split()))
kai = 0
if B <= N:
	kai = int(A*(B-1)/B)
else:
	kai = int(A*N/B)
print(kai)