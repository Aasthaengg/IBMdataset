#import math
#import bisect
#import numpy as np
#import itertools
#import copy
import sys

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

def main():
    a = int(input())
    s = input()

    if a >= 3200:
        print(s)
    else:
        print('red')

if __name__ == '__main__':
    main()