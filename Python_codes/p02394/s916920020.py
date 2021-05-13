import sys

H,W,x,y,r = map(int, raw_input().split())

if (x + r) <= H and (x - r) >= 0:
    if (y + r) <= W and (y - r) >= 0:
        print "Yes"
    else:
        print "No"
else:
    print "No"