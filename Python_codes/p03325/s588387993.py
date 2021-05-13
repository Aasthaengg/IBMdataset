def resolve():
	n = int(input())
	a = list(map(int, input().split()))
	ans = 0
	for i in a:
		if i % 2:
			continue
		while i % 2 == 0:
			ans += 1
			i /= 2
	print(ans)
resolve()