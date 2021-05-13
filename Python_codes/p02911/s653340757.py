import sys

# import bisect
# import numpy as np
from collections import deque
# map(int, sys.stdin.read().split())
# import heapq
#import bisect
#import math

from collections import Counter


def input():
    return sys.stdin.readline().rstrip()


def main():
    N,K,Q =map(int,input().split())
    A =[]
    for i in range(Q):
        A.append(int(input()))
    c = Counter(A)
    for i in range(N):
        if K-Q+c[i+1] >0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
