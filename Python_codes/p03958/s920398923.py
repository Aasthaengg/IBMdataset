K, T = map(int, input().split())
A = list(map(int, input().split()))

A = sorted(A)

Amax = A[-1]

Atwo = sum(A)-Amax

if T == 1:
	print(K-1)
	exit()
if T ==2:
	print(max(A[-1]-1-Atwo, 0))
	exit()

if Amax-1 > Atwo:
	print(Amax-1-Atwo)
else:
	print(0)