import sys
import math

A,B,C,D = map(int, input().split())
def lcm(x, y):
    return (x * y) // math.gcd(x, y)


maru1 = B // C
maru2 = (A-1) // C

maru3 = B // D
maru4 = (A-1) // D

maru5 = B // lcm(C,D)
maru6 = (A-1) // lcm(C,D)

ans_tmp = ((maru1-maru2)+(maru3-maru4)) - (maru5-maru6)
ans = (B-A+1) - ans_tmp

print(ans)