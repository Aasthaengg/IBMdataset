N = int(input())
A = list(map(int, input().split()))

steps = 0
steps_list = []
for i in range(1,N):
	if A[i] < A[i-1]:
		steps_list.append(A[i-1] - A[i])
		A[i] += A[i-1] - A[i]
print(sum(steps_list))
