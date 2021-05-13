Indata = [int(i) for i in input().split()]
W,H,x,y,r = [int(i) for i in Indata]
x_right = x+r
x_left = x-r
y_on = y+r
y_under = y-r

if x_right>W or x_left<0 or y_on>H or y_under<0:
    print("No")
else:
    print("Yes")
