from math import degrees,atan2
a,b,x = map(int, input().split())
ans = 0
if (a*a*b/2 >= x):
    ans = degrees(atan2(a*b*b,2*x))
else:
    x = a*a*b - x
    ans = degrees(atan2(2*x,a*a*a))

print(ans)
