import sys, math
from functools import lru_cache
from collections import defaultdict, Counter
import bisect
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
    K, A, B = mi()

    if B <= A+2:
        print(K+1)
        return

    x = max(0, (K-(A-1))//2)
    y = K-2*x

    print((B-A)*x+y+1)
    

if __name__ == '__main__':
    main()
