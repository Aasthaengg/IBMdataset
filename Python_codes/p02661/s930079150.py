def resolve():
	from statistics import median
	import sys
	input = sys.stdin.readline
	n = int(input())
	ab = [list(map(int, input().split())) for i in range(n)]
	mina = median(i[0] for i in ab)
	maxb = median(i[1] for i in ab)
	abrange = maxb - mina
	if n%2 == 0:
		print(int(abrange*2 + 1))
	else:
		print(int(abrange + 1))
resolve()