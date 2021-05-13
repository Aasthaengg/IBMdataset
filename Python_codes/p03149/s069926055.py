N = list(map(int, input().split()))
N.sort(reverse=False)

if N == [1, 4, 7, 9]:
	print('YES')
else:
	print('NO')