from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A, B = map(int, input().split())

    print('Possible') if not A%3 or not B%3 or not (A+B)%3 else print('Impossible')

if __name__ == '__main__':
    main()