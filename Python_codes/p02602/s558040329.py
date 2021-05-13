N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

s, e = 0, K
while e < N:
	if A[s] < A[e]:
		print('Yes')
	else:
		print('No')
	s += 1
	e += 1