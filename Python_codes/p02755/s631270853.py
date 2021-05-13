import math
from math import gcd
INF = float("inf")

import sys
input=sys.stdin.readline
import itertools

def main():
    a,b = map(float, input().split())
    for i in range(2000):
        if math.floor(i*0.08) == a and math.floor(i*0.1) == b:
            print(i)
            exit()
    print(-1)

if __name__=="__main__":
    main()
