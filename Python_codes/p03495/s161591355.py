import sys
from collections import Counter

def input():
    return sys.stdin.readline()[:-1]

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N, K = mi()
    A = list(mi())
    c = list(Counter(A).values())
    c.sort()
    print(sum(c[:-K]))


if __name__ == '__main__':
    main()
