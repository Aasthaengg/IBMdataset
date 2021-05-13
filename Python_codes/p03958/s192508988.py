#!/usr/bin/env python3
k, t, *a = map(int, open(0).read().split())
a.sort()
c = [0]
for i in a:
    c.append(c[-1]+i)
print(min(abs(c[-1] - c[i]*2) - (c[-1]!= c[i]*2) for i in range(t+1)))
