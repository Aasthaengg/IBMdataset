W,H,x,y,r = map(int,raw_input().split())
if (x + r <= W) & (x - r >= 0) & (y + r <= H) & (y - r >= 0):
	print "Yes"
else:
	print "No"