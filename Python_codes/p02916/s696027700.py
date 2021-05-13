N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.insert(0,"X")
B.insert(0,"X")
C.insert(0,"X")
stf_c = 0
j = 100
for i in range(1,N+1):
	if A[i] == j+1:
		stf_c += (B[A[i]]+C[j])
		j = A[i]
	else:
		stf_c += B[A[i]]
		j = A[i]
print(stf_c)