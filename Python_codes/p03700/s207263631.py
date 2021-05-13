n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]
 
import math
def ok(x):
    t = 0
    for i in range(n):
        r = h[i] - b*x
        if r < 0:
            continue
        else:
            t += math.ceil(r/(a-b))
    if t <= x:
        return True
    else:
        return False
 
l = 0
r = 10**14+1
while l+1 < r:
    c = (l+r)//2
    if ok(c):
        r = c
    else:
        l = c
print(r)