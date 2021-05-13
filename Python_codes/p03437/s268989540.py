import math
x,y = map(int, input().split())
xy = x*y//(math.gcd(x,y))
if xy > x: print(x)
else: print(-1)