def resolve():
	n = int(input())
	a = [0] + list(map(int, input().split())) + [0]
	s = 0
	for i in range(len(a)-1):
		s += abs(a[i+1] - a[i])
	for i in range(1, len(a)-1):
		ta = abs(a[i+1] - a[i-1])
		tb = abs(a[i] - a[i-1]) + abs(a[i+1] - a[i])
		print(s - (tb-ta))
resolve()