N = int(input())
A = []
for _ in range(N):
	A.append(int(input()))
B = sorted(A, reverse = True)
m1, m2 = B[0], B[1]
for i in range(N):
	if m1 > A[i]:
		print(m1)
	else:
		print(m2)
