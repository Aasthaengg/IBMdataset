A, B, C = map(int, input().split())

c, n = 0, 0
if B < C:
	c += B * 2
	n = C - B
else:
	print(B + C)
	exit()

if A < n:
	print(c + A + 1)
else:
	print(c + n)
