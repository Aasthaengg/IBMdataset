N = int(input())
A = list(map(int, input().split()))

n, count = 1, 0
while n < N:
	if A[n - 1] == A[n]:
		count += 1
		n += 1
	n += 1
print(count)
