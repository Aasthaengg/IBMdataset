from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    x, y = map(int, input().split())

    A = [1,3,5,7,8,10,12]
    B = [4,6,9,11]
    C = [2]

    if x in A and y in A:
        print('Yes')
    elif x in B and y in B:
        print('Yes')
    elif x in C and y in C:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()