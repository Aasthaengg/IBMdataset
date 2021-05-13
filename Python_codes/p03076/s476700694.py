#!/usr/bin/env python3
*a, = map(int, open(0).read().split())
ans = 0
m = 10
for i in a:
    if i % 10 != 0:
        m = min(m, i % 10)
        ans += i//10*10 + 10
    else:
        ans += i//10*10
print(ans-10+m)
