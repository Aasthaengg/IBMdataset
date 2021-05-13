n = map(int, raw_input().split())

W = n[0]
H = n[1]
x = n[2]
y = n[3]
r = n[4]

if ((x-r)<0 or (x+r)>W or (y-r)<0 or (y+r)>H):
	print "No"
else:
	print "Yes"