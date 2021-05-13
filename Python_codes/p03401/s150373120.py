#pypyは内包表記使わない, rstrip注意
#提出前に見返すこと！
def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10000000)
    from collections import Counter, deque
    #from collections import defaultdict
    from itertools import combinations, permutations, accumulate
    #from itertools import product
    from bisect import bisect_left,bisect_right
    import heapq
    from math import floor, ceil
    #from operator import itemgetter

    #inf = 10**17
    #mod = 1000000007

    N = int(input())
    A = [0] + list(map(int, input().split())) + [0]
    diff = []
    for i in range(1, N+1):
        if A[i-1]<A[i] and A[i+1]<A[i]:
            diff.append((A[i]-max(A[i-1], A[i+1]))*2)
        elif A[i-1]>A[i] and A[i+1]>A[i]:
            diff.append((min(A[i-1], A[i+1])-A[i])*2)
        else:
            diff.append(0)
    res = 0
    for i in range(N+1):
        res += abs(A[i+1]-A[i])
    for i in diff:
        print(res-i)

if __name__ == '__main__':
    main()