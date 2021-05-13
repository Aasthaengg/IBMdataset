import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

from math import atan2, degrees
a, b, x = mapint()
if x<=a*a*b/2:
    leng = x/b/a*2
    s = atan2(b, leng)
    print(degrees(s))
else:
    x = a*a*b-x
    leng = x/a/a*2
    s = atan2(a, leng)
    print(90-degrees(s))