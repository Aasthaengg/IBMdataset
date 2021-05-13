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

# 最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

def main():
    a, b = map(int, input().split())
    print(lcm(a, b))



if __name__ == '__main__':
    main()

