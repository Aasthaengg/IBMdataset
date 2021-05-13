import warnings

data = map(float, raw_input().split())

w = data[0]
h = data[1]
x = data[2]
y = data[3]
r = data[4]

if (x >= r and x <= (w - r) and y >= r and y <= (h - r)):
	print "Yes"
else:
	print "No"