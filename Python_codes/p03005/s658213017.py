# A - Ball Distribution
N, K = map(int, input().split())

if K == 1:
	print(0)
else:
	max = N - (K - 1)
	print(max - 1)