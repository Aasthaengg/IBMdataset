import sys
from math import floor,ceil
K=int(input())
A=[int(i) for i in input().split()]
B=A[::-1]
a,b=2,2
for i in range(0,K):
    x=B[i]
    c = ceil(a / x) * x
    if a<=c<=b:
        a = c
        b = floor(b / x) * x + x -1
    else:
        print(-1)
        sys.exit()
    #print(a,b,c,x)
print(a,b)