N, K = map(int, input().split())
if 2*N < K:
	print(0)
else:
	kot = (N//K)**3
	if K%2: # odd
		print(kot)
	elif N%K < K//2: # even
		print((N//K)**3 + kot)
	else:
		print((N//K + 1)**3 + kot)