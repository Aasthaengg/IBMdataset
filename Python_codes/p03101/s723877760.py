H,W=[int(i) for i in input().split()]
h,w=[int(i) for i in input().split()]

if(h>=H or w>=W):
    print(0)
else:
    print((H-h)*(W-w))

