N = input()
A = N[::-1]
#print(N)
#print(A)
cont = 0
for i in range(len(N)):
	if N[i] > A[i]:
		cont+=1
print(cont)