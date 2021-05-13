#coding: utf-8

import bisect

n = int(input())
a = [int(n) for n in input().split()]
b = [int(n) for n in input().split()]
c = [int(n) for n in input().split()]

a.sort()
b.sort()
c.sort()

ba = []
baccum = []
tmp = 0
for bb in b:
    ba.append(bisect.bisect_right(a, bb-1))
    tmp += ba[-1]
    baccum.append(tmp) 

cb = []
for cc in c:
    cb.append(bisect.bisect_right(b, cc-1))

ret = 0
for cc in cb:
    if cc == 0:
        continue
    ret += baccum[cc-1] 

print(ret)

