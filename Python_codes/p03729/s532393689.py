from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A,B,C = input().split()

    print('YES') if A[-1] == B[0] and B[-1] == C[0] else print('NO')

if __name__ == '__main__':
    main()