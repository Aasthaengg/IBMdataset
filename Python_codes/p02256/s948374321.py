x,y = list(map(int,input().split()))

###??????x >= y
if y>x:x,y = y,x

while x % y !=0:
    x = x%y
    if y>x:x,y = y,x
print(y)