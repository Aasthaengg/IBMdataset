N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

count = 0

for i in range (0, N):
	if A[i] >= B[i]:
		count+=B[i]
	else:
		B[i]-=A[i]
		count+=A[i]
		if A[i+1] >= B[i]:
			count+=B[i]
			A[i+1]-=B[i]
		else:
			count+=A[i+1]
			A[i+1]=0

print(count)