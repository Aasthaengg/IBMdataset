import math 
import numpy
n, x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
ans = 0
for num, val in enumerate(a):
    x -= val
    if x >= 0:
        ans += 1
    else:
        break
else:
    if x > 0:
        ans -= 1
    else:
        pass
print(ans)