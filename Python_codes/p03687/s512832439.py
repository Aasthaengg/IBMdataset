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

    s = input().rstrip()
    ss = set(s)

    def test(s, ss):
        res = 0
        while len(set(s)) > 1:
            temp = ''
            for i in range(len(s)-1):
                if s[i] == ss or s[i+1] == ss:
                    temp += ss
                else:
                    temp += s[i]
            s = temp[:]
            res += 1

        return res

    res = 10000000000
    for i in ss:
        res = min(res, test(s, i))
    print(res)

if __name__ == '__main__':
    main()