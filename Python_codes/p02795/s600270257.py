import math

h = int(input())
w = int(input())
n = int(input())
ans = 0
if h < w:
    ans = math.ceil(n/w)
else:
    ans = math.ceil(n/h)

print(ans)

