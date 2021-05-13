w,h,x,y = [int(x) for x in input().split()]

if x * 2 == w and y * 2 == h:
    print((w*h)/2, 1)
else:
    print((w*h)/2, 0)