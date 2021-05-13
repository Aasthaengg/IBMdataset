import sys
import copy
a = [int(c) for c in input().split()]
N=a[0]
x=a[1]
a = [int(c) for c in input().split()]
a.sort()
for i in range(N):
    x-=a[i]
    if x<0:
        print(i)
        sys.exit(0)
    elif x==0:
        print(i+1)
        sys.exit(0)

print(N-1)