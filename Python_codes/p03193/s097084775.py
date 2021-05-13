import sys, math
from functools import lru_cache
import numpy as np
import heapq
from collections import defaultdict
sys.setrecursionlimit(10**9)
MOD = 10**9+7

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


def main():
    N, H, W = mi()
    A, B = i2(N)
    
    cnt = 0
    for a, b in zip(A, B):
        if a >= H and b >= W:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
