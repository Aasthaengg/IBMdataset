import math
a, b, x = map(int, input().split())

if (a*a*b)/2 > x:
    ans = 90-math.degrees(math.atan((2*x)/(a*b*b)))
else:
    ans = math.degrees(math.atan(2*b/a - 2*x/(a*a*a)))

print(ans)
