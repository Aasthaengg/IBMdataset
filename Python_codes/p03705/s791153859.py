N, A, B = map(int, input().split())
if N == 1:
	if A == B: print(1)
	else: print(0)
	exit()
if A > B:
	print(0)
	exit()
min = A + B + ((N - 2) * A)
max = A + B + ((N - 2) * B)
print(max - min + 1)