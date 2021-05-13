import math, sys
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque
from copy import deepcopy
from functools import lru_cache
from heapq import heapify, heappop, heappush
from itertools import accumulate, combinations, permutations
input = sys.stdin.readline
mod = 10**9 + 7
ns = lambda: input().strip()
ni = lambda: int(input().strip())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

def main():
    n = ni()

    e = [0] * (n + 1)

    def num(m):
        return len(list(filter(lambda x: x>= m-1, e)))

    for i in range(2, n+1):
        cur = i
        for j in range(2, i+1):
            while cur % j == 0:
                e[j] += 1
                cur //= j
    
    print(num(75) + num(25)*(num(3) - 1) + num(15)*(num(5) - 1)
        + num(5)*(num(5) - 1)*(num(3) - 2) // 2)


if __name__ == '__main__':
    main()