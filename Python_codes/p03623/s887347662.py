x, a,b = map(int, input().split())
xa = abs(a-x)
xb = abs(b-x)
if xa > xb:
	print('B')
else:
	print('A')