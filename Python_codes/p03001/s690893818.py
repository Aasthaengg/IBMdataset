W,H,x,y = map(int,input().split())

_maxarea = W*H/2
mul_judge = 0

if x == W/2 and y == H/2:
    mul_judge = 1

print(str(_maxarea)+' '+str(mul_judge))