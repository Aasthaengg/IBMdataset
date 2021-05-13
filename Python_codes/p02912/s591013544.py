from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    A = [-1 * a for a in A]
    heapify(A)

    for _ in range(M):
        tmp = heappop(A)
        heappush(A, -(-tmp // 2))
    
    print(-sum(A))

if __name__ == '__main__':
    main()