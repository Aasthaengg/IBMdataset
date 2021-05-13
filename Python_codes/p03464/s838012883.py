k=int(input())
a=[int(j) for j in input().split()]
if a[-1]!=2:
    print(-1)
    exit()

import math

amin=2
amax=2
for i in range(k)[::-1]:
    amin+=(-amin)%a[i]
    amax-=amax%a[i]
    amax+=a[i]-1

if amin>amax:
    print(-1)
else:
    print(amin,amax)



