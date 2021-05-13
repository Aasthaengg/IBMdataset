a, b = map(int, input().split())

if a == 1:
	print(b)
else:
	ans = 1
	for i in range(a-1):
		ans *= (b-1)
	print(ans * b)