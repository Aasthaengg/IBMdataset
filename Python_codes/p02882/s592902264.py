import math

a, b, x = map(int, input().split())

if  2 * x <= a ** 2 * b:
    ans = math.atan(a*b**2/2/x)
else:
    ans = math.atan(2*(a**2*b-x)/a**3)
print(math.degrees(ans))