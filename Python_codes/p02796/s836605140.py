def resolve():
	n = int(input())
	robots = [list(map(int, input().split())) for _ in range(n)]
	robots.sort(key=lambda x: x[0] + x[1])
	t = robots[0][0] + robots[0][1]
	a = n
	for i in range(1, n):
		if t <= robots[i][0] - robots[i][1]:
			t = robots[i][0] + robots[i][1]
		else:
			a -= 1
	print(a)
resolve()