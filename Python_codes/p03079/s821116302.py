L = list(map(int,input().split()))
if all([L[0] == L[i] for i in range(3)]):
	print('Yes')
else:
	print('No')