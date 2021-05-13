import numpy as np
def solve(s):
    h = int(np.sqrt(s))
    if h**2 < s:
        h += 1
    d = h**2 - s
    if d == 0:
        x, y = 0, 0
    else:
        x, y = 1, d
    return " ".join(map(str, [0,0,x,h,h,y]))

s = int(input())
print(solve(s))