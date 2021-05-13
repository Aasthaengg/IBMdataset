W, H, x, y, r = map(int, raw_input().split())

up = y + r
down = y - r
left = x - r
right = x + r

if up <= H and down >= 0 and left >= 0 and right <= W:
	print "Yes"

else:
	print "No"