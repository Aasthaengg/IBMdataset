def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left,bisect_right
    from heapq import heapify, heappop, heappush
    import math
    #from math import gcd

    #inf = 10**17
    #mod = 10**9 + 7

    n = int(input())
    a = list(map(int, input().split()))
    b = [a[0]]
    for i in a:
        if b[-1] == i:
            continue
        b.append(i)
    res = 1
    if len(b) <= 2:
        print(res)
    else:
        i = 1
        while i <= len(b)-2:
            if b[i] == max(b[i-1], b[i], b[i+1]) or b[i] == min(b[i-1], b[i], b[i+1]):
                res += 1
                i += 1
            i += 1
        print(res)

if __name__ == '__main__':
    main()
