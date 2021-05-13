def resolve():
	input()
	s = list(map(int, input().split()))
	print(max(s) - min(s))
resolve()