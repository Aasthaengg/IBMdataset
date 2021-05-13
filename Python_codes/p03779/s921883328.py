import sys, math
from collections import defaultdict
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
    X = ii()
    s = 0
    i = 1
    while s < X:
        s += i
        i += 1
    print(i-1)

if __name__ == '__main__':
    main()