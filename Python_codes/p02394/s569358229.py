W,H,x,y,r = map(int,raw_input().split())
if x >= r and x <= W-r and y >= r and y<= H-r:
	print "Yes"
else:
	print "No"