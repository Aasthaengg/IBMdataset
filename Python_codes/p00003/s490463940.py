N = input()
for i in range(N):
	a, b, c = map(int, raw_input().split())
	t1 = a**2 + b ** 2 == c ** 2
	t2 = b**2 + c ** 2 == a ** 2
	t3 = c**2 + a ** 2 == b ** 2
	if t1 or t2 or t3:
		print("YES")
	else:
		print("NO")