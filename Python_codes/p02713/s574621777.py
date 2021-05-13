# coding: utf-8
import itertools
import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)
    
def main():
    k = int(input())
    array = list(range(1, k+1))
    ans = sum(array)
    for i in range(2, 4):
        for x in itertools.combinations(array, i):
            x = list(x)
            tmp = gcd(*x)
            ans += tmp * 6
    print(ans)
    
main()
