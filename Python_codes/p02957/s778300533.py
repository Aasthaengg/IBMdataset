A, B = list(map(int, input().split()))
if (A + B) % 2 != 0:
	print('IMPOSSIBLE')
else:
	K = (A + B) // 2
	print(K)
