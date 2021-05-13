import math
import fractions
from functools import reduce
import sys
input = sys.stdin.readline


def main():
    n, m = input_list()
    s = input()
    t = input()
    baisuu = lcm_base(n, m)
    ans = {}
    for i in range(1, n+1):
        index = (i - 1) * (baisuu//n) + 1
        ans[index] = s[i-1]

    for i in range(1, m+1):
        index = (i - 1) * (baisuu//m) + 1
        w = t[i-1]
        if index in ans:
            if ans[index] != w:
                print(-1)
                exit(0)
        else:
            ans[index] = w

    print(baisuu)


def input_list():
    return list(map(int, input().split()))

def lcm_base(x, y):
    return (x * y) // fractions.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

def gcd(*numbers):
    return reduce(fractions.gcd, numbers)

def gcd_list(numbers):
    return reduce(fractions.gcd, numbers)

if __name__ == "__main__":
    main()
