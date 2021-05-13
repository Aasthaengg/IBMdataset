a = map(int, raw_input().split())
W = a[0]
H = a[1]
x = a[2]
y = a[3]
r = a[4]

if r <= x and x <= W - r and r <= y and y <= H - r:
    print "Yes"
else:
    print "No"