w,h,x,y,r = map(int, raw_input().split())

if x-r >= 0 and y-r >= 0:
    if x+r <= w and y+r <= h:
        print 'Yes'
    else:
        print 'No'
else:
    print 'No'