import sys
from math import *
from fractions import gcd
readints=lambda:map(int, input().strip('\n').split())



m,k = readints()

if k>=2**m:
    print(-1)
    sys.exit(0)


if m==1:
    if k==0:
        print('0 0 1 1')
    else:
        print(-1)
    sys.exit(0)


ans = []
for i in range(2**m):
    if i!=k:
        ans.append(i)

ans.append(k)
i=2**m-1
while i>=0:
    if i!=k:
        ans.append(i)
    i-=1
ans.append(k)


print(' '.join([str(i) for i in ans]))
