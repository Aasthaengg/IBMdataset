import sys

# import bisect
# import numpy as np
# from collections import deque
from collections import deque
# map(int, sys.stdin.read().split())
# import heapq
#import bisect
#import math


def input():
    return sys.stdin.readline().rstrip()


def main():
    N = int(input())
    A = list(map(int, input().split()))
    l = list()
    for i in range(N):
        l.append((A[i],i+1))
    l.sort()
    for i in range(N):
        print(l[i][1],end=" ")

if __name__ == "__main__":
    main()
