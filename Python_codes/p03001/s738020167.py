W,H,x,y = map(int,input().split())

#print(W,H,x,y)
area =  "{0:.6f}".format(float(W*H/2))
if x == W/2 and y == H/2:
    print(area,1)
else:
    print(area,0)