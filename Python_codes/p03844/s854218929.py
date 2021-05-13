from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A, op, B = input().split()

    print(int(A) + int(B)) if op == '+' else print(int(A) - int(B))

if __name__ == '__main__':
    main()