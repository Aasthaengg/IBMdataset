W,H,x,y,r=[int(x) for x in input().split()]
print('Yes' if 0<=x-r<=x+r<=W and 0<=y-r<=y+r<=H else 'No')
