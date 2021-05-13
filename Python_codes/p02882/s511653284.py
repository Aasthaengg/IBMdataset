from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools
import queue
from collections import deque
from fractions import Fraction


def get_max(a, b, theta):
    kari = b * math.tan(math.radians(90 - theta))
    if kari > a:
        S = (a * b) - (a * (a * math.tan(math.radians(theta))) / 2)
    else:
        S = (kari * b) / 2
    max_water = S * a
    return max_water




def main():
    a, b, x = map(int, input().split())
    left, right = 0, 90

    for i in range(10000):
        half = (left + right) / 2
        max_water = get_max(a, b, half)
        if max_water >=x:
            left = half
        else:
            right = half

    print(left)





if __name__ == '__main__':
    main()

