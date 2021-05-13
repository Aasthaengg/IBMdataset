D,N = map(int,input().split())
A = [int(i) for i in range(1,100)] + [101]
B = [int(i*100) for i in range(1,100)] + [10100]
C = [int(i*10000) for i in range(1,100)] + [1010000]

if D == 0:
	print(A[N-1])
elif D == 1:
	print(B[N-1])
else:
	print(C[N-1])