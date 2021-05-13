from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    s1, s2, s3 = input().upper().split()

    print(s1[0] + s2[0] + s3[0])

if __name__ == '__main__':
    main()