import sys
from collections import deque, Counter, defaultdict
from itertools import permutations
import heapq


def resolve():
    X, Y = map(int, sys.stdin.readline().strip().split())
    ans = 0
    while X <= Y:
        ans += 1
        X <<= 1

    print(ans)


if __name__ == "__main__":
    resolve()
