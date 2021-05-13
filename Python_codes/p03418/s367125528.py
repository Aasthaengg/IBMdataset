import sys
from collections import defaultdict, deque
from functools import reduce
import math

input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    count = 0
    for b in range(K+1, N+1):
        count += max((b - K), 0) * (N // b) + max(N % b - K + 1, 0)
    if K == 0:
        count = N*N
    print(count)

if __name__ == '__main__':
    main()
