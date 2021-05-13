N = int(input())
A = list(map(int, input().split()))
cnt = 1
	
status = 0
for i in range(N-1):
	if A[i] > A[i+1]:
		if status == 0: status = 1
		elif status == -1:
			status = 0
			cnt += 1
	elif A[i] < A[i+1]:
		if status == 0: status = -1
		elif status == 1:
			status = 0
			cnt += 1
print(cnt)