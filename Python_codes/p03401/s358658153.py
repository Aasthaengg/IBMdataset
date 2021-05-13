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
    a = nl()

    arr = [0]
    arr.extend(a)
    arr.append(0)
    total = sum([abs(arr[i-1] - arr[i]) for i in range(1, n+2)])

    for i in range(1, n+1):
        #print(abs(arr[i-1] - arr[i]), abs(arr[i-1] - arr[i+1]))
        ans = total - abs(arr[i-1] - arr[i]) - abs(arr[i] - arr[i+1]) + abs(arr[i-1] - arr[i+1])
        print(ans)
        

if __name__ == '__main__':
    main()