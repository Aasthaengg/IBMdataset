num = raw_input()
num = num.split()
result = True
w, h, x, y, r = int(num[0]), int(num[1]), int(num[2]), int(num[3]), int(num[4])

if x < r or (w - r) < x:
	result = False

if y < r or (h - r) < y:
	result = False

if result:
	print "Yes"
else:
	print "No"