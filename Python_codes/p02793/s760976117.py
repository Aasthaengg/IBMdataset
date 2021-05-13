import fractions
from functools import reduce

divisor = 10**9 + 7

def lcm(x,y):
    return (x*y // fractions.gcd(x,y))

def lcm_list(numbers):
    return reduce(lcm, numbers, 1)

N = int(input())
numbers = [int(i) for i in input().split()]

lowest_common_multiple = lcm_list(numbers)

cnt = 0
for i in numbers:
    cnt += lowest_common_multiple // i
    
print(cnt%divisor)