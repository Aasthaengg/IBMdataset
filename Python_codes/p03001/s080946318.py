w,h,x,y = map(int,input().split())

S = (w*h)/2
if 2*x ==w and 2*y == h:
    j = 1
else:j = 0

print(S,j)