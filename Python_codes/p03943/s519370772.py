from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    a, b, c = map(int, input().split())

    if a == b + c or b == a + c or c == a + b:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()