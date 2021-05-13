a, b, c, k = map(int, input().split())

if k % 2 == 0:
	diff = a - b
else:
	diff = -a + b

print(diff) if diff <= 10 ** 18 else print('Unfair')