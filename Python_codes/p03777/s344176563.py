from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    a, b = input().split()

    print('H') if (a == 'H' and b == 'H') or (a == 'D' and b == 'D') else print('D')

if __name__ == '__main__':
    main()