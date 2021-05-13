a, b, c, k = map(int, input().split())
if abs(a-b) > 10 ** 18:
	print('Unfair')
else:
	print(a - b if k % 2 == 0 else b - a)