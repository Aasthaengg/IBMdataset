import sys
from collections import deque
import itertools
from collections import deque
sys.setrecursionlimit(10 ** 9)
import heapq
import numpy as np

# map(int, sys.stdin.read().split())


def input():
    return sys.stdin.readline().rstrip()


def main():
    N,M = map(int,input().split())
    A = list(map(lambda x: int(x)*-1,sys.stdin.read().split()))
    heapq.heapify(A)

    for _ in range(M):
        temp = heapq.heappop(A)
        temp=-temp//2
        heapq.heappush(A,-temp)
    print(-sum(A))




    pass



if __name__ == "__main__":
    main()
