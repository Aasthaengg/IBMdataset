import math

a, b, x = map(int,input().split())
lb = 0
ub = 90

while ub - lb > 0.5 * 10**-6:
    theta = (lb+ub) / 2
    tt = math.tan(math.radians(theta))
    tt9 = math.tan(math.radians(90 - theta))
    
    if b * tt9 >= a:
        y = a*a*b - a * a*a*tt/2 - x
        if y < 0:
            ub = theta
        else:
            lb = theta
    else:
        y = a * b*b*tt9/2 - x
        if y < 0:
            ub = theta
        else:
            lb = theta
print(theta)