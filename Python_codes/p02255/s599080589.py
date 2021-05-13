import sys

N = int(raw_input())
A = map(int, raw_input().split())
a_str = map(str, A)
print(" ".join(a_str))
for i in range(1, len(A)):
	key = A[i]
	j = i - 1
	while j >= 0 and A[j] > key:
		A[j + 1] = A[j]
		j -= 1
	A[j + 1] = key
	a_str = map(str, A)
	print(" ".join(a_str))