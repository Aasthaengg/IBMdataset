from math import fabs
x,y = map(int, input().split())
if y >= x >= 0: 
    print(int(fabs(y-x)))
elif 0 >= y >= x:
    print(int(fabs(y-x))) 
elif x > y > 0: 
    print(int(x - y + 2))
elif 0 > x > y:
    print(int(x - y + 2)) 
else:
    print(int(fabs(fabs(x)-fabs(y)) + 1))