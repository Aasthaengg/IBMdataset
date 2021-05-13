from fractions import gcd
# from datetime import date, timedelta
from heapq import*
import math
from collections import defaultdict, Counter, deque
from bisect import *
import itertools
import fractions
import sys
sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7
# input = sys.stdin.readline


def lcm(a, b):
    return a * b / fractions.gcd(a, b)


def main():
    a, b = map(int, input().split())
    grid = [["." for i in range(100)] for j in range(100)]
    for i in range(50):
        for j in range(100):
            grid[i][j] = "#"

    for i in range(0, 50, 2):
        for j in range(0, 100, 2):
            if a == 1:
                break
            grid[i][j] = "."
            a -= 1
        if a == 1:
            break

    for i in range(51, 100, 2):
        for j in range(0, 100, 2):
            if b == 1:
                break
            grid[i][j] = "#"
            b -= 1

        if b == 1:
            break
    print(100,100)
    for i in range(100):
        print("".join(map(str, grid[i])))
        





if __name__ == '__main__':
    main()
