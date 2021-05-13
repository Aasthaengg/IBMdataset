def resolve():
	x, y = map(int, input().split())
	ans = 1
	while True:
		if x * 2 > y:
			break
		ans += 1
		x *= 2
	print(ans)
resolve()