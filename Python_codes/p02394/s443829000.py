w, h, x, y, r= map(int, raw_input().split())
if (r <= x <= w-r) and (r <= y <= h - r):
	print 'Yes'
else:
	print 'No'