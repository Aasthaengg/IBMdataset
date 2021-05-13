W, H, x, y, r = map(int, raw_input().split())
left = x - r
right = x + r
top = y + r
bottom = y - r

if (left < 0) | (W < right) | (bottom < 0) | (H < top):
    print "No"
else:
    print "Yes"