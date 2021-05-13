w,h,x,y,r = map(int,input().split())

if (x-r) < 0 or (x+r) > w:
    print('No')
elif (y-r) < 0 or (y+r) > h:
    print('No')
    
else:
    print('Yes')
