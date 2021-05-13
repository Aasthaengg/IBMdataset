def resolve():
	n = int(input())
	ans = 0
	for _ in range(n):
		s, e = map(int, input().split())
		ans += e - s + 1
	print(ans)
resolve()