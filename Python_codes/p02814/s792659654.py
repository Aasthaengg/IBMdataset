from fractions import gcd
from functools import reduce
import sys

N, M = map(int, input().split())
alist = list(map(lambda k: int(k) // 2, input().split()))

numdic = {}

def lcm(x, y):
    return (x * y) // gcd(x,y)

def lcm_list(numbers):
    return reduce(lcm, numbers, 1)

lcmnum = lcm_list(alist)

for i in alist:
    if (lcmnum//i)%2==0:
        print(0)
        sys.exit()

pmax = M // lcmnum
pmax = pmax - 1 if pmax % 2 == 0 else pmax

print((pmax+1)//2)
