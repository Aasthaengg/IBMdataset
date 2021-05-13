N = int(input())

count = 10000000

for i in range (1, N//2+2):
	A = str(i)
	B = str(N-i)
	temp = 0
	for j in range (0, len(A)):
		temp+=int(A[j])
	for j in range (0, len(B)):
		temp+=int(B[j])
	count = min(count, temp)

print(count)