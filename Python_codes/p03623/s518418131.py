from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    x, a, b = list(map(int, input().split()))

    print('A') if abs(x - a) < abs(x - b) else print('B')

if __name__ == '__main__':
    main()