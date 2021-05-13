import math
from functools import reduce

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)
    
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

if __name__ == '__main__':

    n = int(input())
    A = list(map(int,input().split()))

    ans = lcm(*A) - 1

    tmp = 0
    for i in A:
        tmp += ans % i
    print(tmp)
