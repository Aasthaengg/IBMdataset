# coding: utf-8
import math
a, b = map(int, input().split())
ans = 1
now_consent = a
plusplug = a - 1
if b == 1:
  print(0)
elif a >= b:
    print(1)
elif a < b:
    other = b - a
    ans += math.ceil(other / plusplug)
    print(ans)