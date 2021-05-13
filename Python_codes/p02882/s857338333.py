import math
a, b, x = map(int, input().split())
if x*2 <= a**2*b:
    ans = math.degrees(math.atan(2*x/a/b**2))
    print(90 - ans)
else:
    ans = math.degrees(math.atan(2*b/a - 2*x/a**3))
    print(ans)