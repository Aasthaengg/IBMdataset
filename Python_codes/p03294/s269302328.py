import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

n = int(input())
l = list(map(int,input().split()))

k = (lcm_list(l))-1

ans = [0]*n
for i in range(n):
    ans[i] = k%l[i]

print(sum(ans))