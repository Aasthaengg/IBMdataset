W,H,x,y,r = map(int,raw_input().split())
print ['No','Yes'][r<=x<=W-r and r<=y<=H-r]