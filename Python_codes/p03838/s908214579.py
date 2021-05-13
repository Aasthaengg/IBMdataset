x, y = map(int, input().split())

if x == y:
	res = 0
elif x < y:
	if (0 <= x and 0 <= y) or (x <= 0 and y <= 0):
		res = y - x
	else:
		if abs(x) >= y:
			res = abs(x) - y + 1
		else:
			res = y - abs(x) + 1
else:
	if 0 < x and 0 < y:
		res = x - y + 2
	elif x < 0 and y < 0:
		res = abs(y) - abs(x) + 2
	else:
		if x >= abs(y):
			res = x - abs(y) + 1
		else:
			res = abs(y) - x + 1
		
print(res)