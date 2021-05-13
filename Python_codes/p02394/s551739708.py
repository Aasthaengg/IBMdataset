num = map(int, raw_input().split())
W = num[0]
H = num[1]
x = num[2]
y = num[3]
r = num[4]

if x-r >= 0 and x+r <= W:
    if y-r >= 0 and y+r <= H:
        print "Yes"
    else:
        print "No"
else:
    print "No"