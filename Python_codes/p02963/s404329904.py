import math
s = int(input())
t = int(math.sqrt(s) // 1)
if s == t**2:
    print(0, 0, 0, t, t, 0)
else:
    t += 1
    e = t * t - s
    print(0, 0, t, e, 1, t)
