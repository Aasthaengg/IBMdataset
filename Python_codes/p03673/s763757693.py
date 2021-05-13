n = int(input())
A = list(map(int, input().split()))
if len(A) % 2:
	print(*(A[-1::-2] + A[1::2]))
else:
	print(*(A[-1::-2] + A[::2]))