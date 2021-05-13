from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    A, B, C = map(int, input().split())
    K = int(input())

    for _ in range(K):
        if B <= A:
            B *= 2
        elif C <= B:
            C *= 2
    
    if A < B < C:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()