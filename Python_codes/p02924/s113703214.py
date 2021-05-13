#import math
#import bisect
#import numpy as np
#import itertools
#import copy
import collections
import sys

ipti = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)

def main():
    n = int(input())
    print((n-1)*n//2)

if __name__ == '__main__':
    main()
