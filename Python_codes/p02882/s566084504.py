from math import degrees, atan, radians
a, b, x = map(int, input().split())

if(x <= 0.5*a*a*b):
    y = x/(0.5*b*a)
    ans = 90-degrees(atan(y/b))
    print(ans)
elif(x == a*a*b):    
    print(0)
else:
    y = x/(0.5*a**2)-b
    ans = 90-degrees(atan((a/(b-y))))
    print(ans)