import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools
from collections import Counter

def main():
    def isPrime(n):
        if n == 2:
            return True
        if n%2 == 0:
            return False
        m = math.floor(math.sqrt(n))+1
        for p in range(3,m,2):
            if n%p == 0:
                return False
        return True

    x = int(input())
    while True:
        if isPrime(x):
            print(x)
            exit()
        x += 1

if __name__=="__main__":
    main()
