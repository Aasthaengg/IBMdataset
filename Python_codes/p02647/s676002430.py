#!/usr/bin/env python3
from collections import deque, Counter
from heapq import heappop, heappush
from bisect import bisect_right
from itertools import accumulate
import math

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    mina = min(A)
    for i in range(K):
        B = [0]*N
        for j in range(N):
            if j-A[j] >= 0:
                B[j-A[j]] += 1
            else:
                B[0] += 1
            if j+A[j]+1 < N:
                B[j+A[j]+1] -= 1
        A = list(accumulate(B[:]))
        mina = mina*2+1
        if mina >= N and A[0] == A[-1] == N:
            break
    print(*A)

if __name__ == "__main__":
    main()
