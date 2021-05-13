import functools
from fractions import gcd
n,k = map(int,input().split())
li = list(map(int,input().split()))
g = functools.reduce(gcd,li)
if k > max(li):
    print("IMPOSSIBLE")
elif g == 1:
    print("POSSIBLE")
else:
    if k % g == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")