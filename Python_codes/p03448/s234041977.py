#!/usr/bin/env python3
a,b,c,x=map(int,open(0).read().split())
ans = 0
for i in range(a+1):
    for j in range(b+1):
        if c*50 >= x - 500*i -100*j >= 0:
            ans += 1
print(ans)
