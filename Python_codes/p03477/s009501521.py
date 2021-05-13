a, b, c, d = map(int, input().split())

l, r = a+b, c+d
if l > r:
	print('Left')
elif r > l:
	print('Right')
else:
	print("Balanced")