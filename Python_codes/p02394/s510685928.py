W, H, x, y, r = map(int, input().split(' '))

flag_x = (x + r <= W) and (x - r >= 0)
flag_y = (y + r <= H) and (y - r >= 0)

if flag_x and flag_y:
	print('Yes')
else:
	print('No')