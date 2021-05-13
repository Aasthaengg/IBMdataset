w, h, x, y, r = map(int, raw_input().split())
if x >= r and y >= r and x+r <= w and y+r <= h:
    print 'Yes'
else:
    print 'No'