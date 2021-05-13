n=int(input())
for i in range(n):
	A=[int(j) for j in input().split()]
	A.sort()
	if A[0]**2+A[1]**2==A[2]**2:
		print("YES")
	else:
		print("NO")