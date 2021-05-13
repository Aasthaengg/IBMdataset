m = map(int,raw_input().split())
w = m[0]
h = m[1]
x = m[2]
y = m[3]
r = m[4]

if 2*r > w or 2*r >h:
 print "No"
else:
 if 0 < x + r <= w and 0 < y + r <= h:
  print "Yes"
 else:
  print "No"