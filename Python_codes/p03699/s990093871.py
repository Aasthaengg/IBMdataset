N = int(input())
A = []
for i in range(N):
	A.append(int(input()))
m = 100
sum = 0
for i in range(N):
	if A[i] % 10 != 0 and m > A[i]:
		m = A[i]
	sum += A[i]
if m == 100:
	print(0)
else:
	if sum % 10 == 0:
		print(sum-m)
	else:
		print(sum)