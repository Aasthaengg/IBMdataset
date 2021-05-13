import sys
from itertools import product

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
    N, K = mi()
    x = list(mi())
    m = 10**100
    for i in range(N-K+1):
        tmp = min(abs(x[i]), abs(x[i+K-1]))+(x[i+K-1]-x[i])
        m = min(m, tmp)
    print(m)


if __name__ == '__main__':
    main()
