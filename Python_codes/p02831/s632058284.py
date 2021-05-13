import sys
input = sys.stdin.readline
import math
from functools import reduce


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)


# 最小公倍数
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

# AでもBでも割り切れる数の最小値、それが最小公倍数だ
A, B = [int(x) for x in input().split()]

ans = lcm(A, B)
print(ans)