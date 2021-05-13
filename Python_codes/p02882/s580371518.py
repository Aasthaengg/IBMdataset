import math
a, b, x = map(int,input().split())
ans = math.atan(2*b/a-2/a/a/a*x) * 180 / math.pi
ans2 = math.atan(a*b*b/x/2) * 180 / math.pi
if a*a*b < 2*x:
    print(ans)
else:
    print(ans2)