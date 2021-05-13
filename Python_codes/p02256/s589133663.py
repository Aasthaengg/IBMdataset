if __name__ == '__main__':
	a, b = input().split()
	a, b = int(a), int(b)
	if a < b:
		x = b
		y = a
	else:
		x = a
		y = b
	while True:
		x, y= y, x % y
		if y == 0:
			print(x)
			break
		else:
			continue
