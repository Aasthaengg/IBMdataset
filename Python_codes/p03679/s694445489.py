from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    X, A, B = map(int, input().split())

    if A - B >= 0:
        print('delicious')
    elif abs(A - B) <= X:
        print('safe')
    else:
        print('dangerous')

if __name__ == '__main__':
    main()