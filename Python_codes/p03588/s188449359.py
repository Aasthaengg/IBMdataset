import sys, math
from collections import deque

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
    N = ii()
    A, B = i2(N)
    print(min(B)+max(A))
        

if __name__ == '__main__':
    main()
