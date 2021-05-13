line = list(map(int,input().split()))
W, H, x, y, r = line[0],line[1],line[2],line[3],line[4]
if r<=x<=W-r and r<=y<=H-r: print('Yes')
else: print('No')