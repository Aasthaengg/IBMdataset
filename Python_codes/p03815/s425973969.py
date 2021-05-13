#!/usr/bin/env python

x = int(input())
t = x-11*(x//11)
if t <= 6:
    if x%11 != 0:
        ans = 2*(x//11)+1
    else:
        ans = 2*(x//11)
else:
    if x%11 != 0:
        ans = 2*(x//11)+2
    else:
        ans = 2*(x//11)+1
print(ans)
