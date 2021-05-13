import math

while True:
	d =0
	n = int(input())
	if n == 0:
		break
	s = list(map(int, input().split()))
	avg = sum(s) / len(s)
	for i in s:
		c = (i - avg) ** 2
		d += c
	a2 = d / len(s)
	print(math.sqrt(a2))

