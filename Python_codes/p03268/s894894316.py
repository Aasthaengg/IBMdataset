import sys, math
from itertools import combinations
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
    N, K = mi()
    if K%2==1:
        print((N//K)**3)
    else:
        print((math.floor((N//(K//2))/2))**3+(math.ceil((N//(K//2))/2))**3)

if __name__ == '__main__':
    main()