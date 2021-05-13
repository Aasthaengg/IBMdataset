import math
from functools import reduce

def LCM_base(x, y):
    return (x * y) // math.gcd(x, y)


# 最小公倍数（リスト引数）
def LCM_list(numbers):
    return reduce(LCM_base, numbers, 1)


N = int(input())
T = [int(input()) for x in range(N)]

lcm = LCM_list(T)
print(lcm)