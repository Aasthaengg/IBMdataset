W,H,x,y,r = [int(i) for i in input().split()]
if 0 <= x-r and x+r <= W and 0 <= y-r and H >= y+r :
    print('Yes')
else :
    print('No')
