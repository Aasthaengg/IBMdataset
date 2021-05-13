import sys, math
from functools import lru_cache
sys.setrecursionlimit(500000)
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
    X, Y = mi()
    pt = 0
    if X == 1:
        pt += 300000
    if X == 2:
        pt += 200000
    if X == 3:
        pt += 100000
    if Y == 1:
        pt += 300000
    if Y == 2:
        pt += 200000
    if Y == 3:
        pt += 100000
    if X == Y == 1:
        pt += 400000

    print(pt)

if __name__ == '__main__':
    main()