import math

a, b, x = map(int, input().split())
t = 2 * b - (2 * x) / (a ** 2)
ans = 0
if t > b:
    t = 2 * x / (a * b)
    ans = math.degrees(math.atan2(b, t))
else:
    ans = math.degrees(math.atan2(t, a))
print(ans)
